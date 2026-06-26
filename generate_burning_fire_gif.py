import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

INPUT_IMAGE = "images/discovery_of_fire.png"
OUTPUT_GIF = "images/discovery_of_fire.gif"

def bilinear_warp(img_np, map_x, map_y):
    H, W, C = img_np.shape
    
    # Clip coordinates to safe bounds
    map_x = np.clip(map_x, 0, W - 2)
    map_y = np.clip(map_y, 0, H - 2)
    
    # Get coordinates of 4 surrounding pixels
    x0 = np.floor(map_x).astype(np.int32)
    x1 = x0 + 1
    y0 = np.floor(map_y).astype(np.int32)
    y1 = y0 + 1
    
    # Interpolation weights
    wa = (x1 - map_x) * (y1 - map_y)
    wb = (map_x - x0) * (y1 - map_y)
    wc = (x1 - map_x) * (map_y - y0)
    wd = (map_x - x0) * (map_y - y0)
    
    wa = np.expand_dims(wa, axis=-1)
    wb = np.expand_dims(wb, axis=-1)
    wc = np.expand_dims(wc, axis=-1)
    wd = np.expand_dims(wd, axis=-1)
    
    # Sample pixels
    p00 = img_np[y0, x0]
    p10 = img_np[y0, x1]
    p01 = img_np[y1, x0]
    p11 = img_np[y1, x1]
    
    # Interpolate
    out = p00 * wa + p10 * wb + p01 * wc + p11 * wd
    return out.astype(np.float32)

def generate_seamless_fire_gif():
    if not os.path.exists(INPUT_IMAGE):
        print(f"Error: Input image {INPUT_IMAGE} not found.")
        return False
        
    img = Image.open(INPUT_IMAGE).convert("RGB")
    W, H = img.size
    img_np = np.array(img).astype(np.float32)
    
    # 1. Define Spatial Mask for Fire Bounding Box (Scaled for 1024x1024)
    # Center of fire: cx = 515, cy = 750
    cx, cy = 515, 750
    rx, ry = 205, 210
    
    # Grid of coordinates
    Y, X = np.mgrid[0:H, 0:W]
    
    # Normalized distance from center of fire
    dist = np.sqrt(((X - cx) / rx)**2 + ((Y - cy) / ry)**2)
    spatial_weight = np.clip(1.0 - dist, 0.0, 1.0)
    # Cosine smoothstep for soft boundary transition
    spatial_weight = (np.cos(np.pi * (1.0 - spatial_weight) / 2.0))**2
    
    # 2. Define Color Mask to select bright flames (warm yellow/orange/white pixels)
    is_fire = (img_np[..., 0] > 140) & (img_np[..., 1] > 80) & (img_np[..., 0] > img_np[..., 2] + 30)
    
    # Smooth the color mask using PIL's Gaussian Blur
    mask_pil = Image.fromarray((is_fire * 255).astype(np.uint8), mode="L")
    mask_pil = mask_pil.filter(ImageFilter.GaussianBlur(radius=15))
    color_weight = np.array(mask_pil).astype(float) / 255.0
    
    # Combined Warp Mask
    warp_mask = color_weight * spatial_weight
    
    # 3. Setup Sparks / Flying Embers (periodic loop parameters, scaled for 1024x1024)
    num_frames = 24
    num_sparks = 20
    sparks = []
    
    np.random.seed(42)
    for i in range(num_sparks):
        # Lifespans are between 8 and 14 frames
        lifetime = np.random.randint(8, 15)
        birth_frame = np.random.randint(0, num_frames)
        
        # Start coordinates near fire base (scaled)
        start_x = np.random.randint(410, 640)
        start_y = np.random.randint(720, 810)
        
        # Speed details (scaled)
        vx_amp = np.random.uniform(2.5, 6.0)
        vx_freq = np.random.uniform(0.3, 0.6)
        vy = np.random.uniform(14.0, 24.0)
        
        size = np.random.uniform(1.5, 3.5)
        
        sparks.append({
            "lifetime": lifetime,
            "birth": birth_frame,
            "x0": start_x,
            "y0": start_y,
            "vx_amp": vx_amp,
            "vx_freq": vx_freq,
            "vy": vy,
            "size": size
        })
        
    frames = []
    
    print("Generating fire animation frames...", flush=True)
    for t in range(num_frames):
        # 4. Horizontal and Vertical Sinusoidal Warping
        # Upward waving phase
        phase_x = (Y / 44.0) - t * (2.0 * np.pi / num_frames)
        phase_y = (Y / 55.0) - t * (2.0 * np.pi / num_frames)
        
        # Calculate displacement fields (scaled amplitudes)
        dx = 10.0 * np.sin(phase_x) * warp_mask
        dy = -8.0 * (1.2 + np.cos(phase_y)) * warp_mask
        
        # Apply Bilinear Warp
        warped_np = bilinear_warp(img_np, X + dx, Y + dy)
        
        # 5. Global/Local Firelight Flicker effect
        # Create a periodic flicker scale
        flicker = 1.0 + 0.05 * np.sin(t * (2.0 * np.pi / 6.0)) + 0.035 * np.sin(t * (2.0 * np.pi / 3.0) + 1.5)
        
        # Apply warm firelight glow modulation outside the active fire zone
        glow_mask = spatial_weight * (1.0 - color_weight)
        
        # Red channel boost
        r_mod = 1.0 + (flicker - 1.0) * 0.9 * glow_mask
        # Green channel boost
        g_mod = 1.0 + (flicker - 1.0) * 0.65 * glow_mask
        # Blue channel
        b_mod = 1.0 + (flicker - 1.0) * 0.15 * glow_mask
        
        warped_np[..., 0] *= r_mod
        warped_np[..., 1] *= g_mod
        warped_np[..., 2] *= b_mod
        
        # Clip values to safe range
        warped_np = np.clip(warped_np, 0.0, 255.0).astype(np.uint8)
        
        # Convert back to PIL for spark drawing and saving
        frame_img = Image.fromarray(warped_np)
        draw = ImageDraw.Draw(frame_img)
        
        # 6. Render Sparks / Glowing Embers
        for spark in sparks:
            # Check if active in this frame (handle looping boundaries)
            age = (t - spark["birth"]) % num_frames
            if age < spark["lifetime"]:
                # Calculate current position
                x = spark["x0"] + spark["vx_amp"] * np.sin(age * spark["vx_freq"])
                y = spark["y0"] - spark["vy"] * age
                
                # Calculate size/fade based on age
                progress = age / spark["lifetime"]
                current_size = spark["size"] * (1.0 - progress * 0.4)
                
                # Interpolate color
                r = 255
                g = int(220 * (1.0 - progress) + 80 * progress)
                b = int(120 * (1.0 - progress) + 20 * progress)
                
                # Draw the spark
                r_spark = current_size
                draw.ellipse([x - r_spark, y - r_spark, x + r_spark, y + r_spark], fill=(r, g, b))
                
        # Downscale to keep GIF size optimized (width=500, height=500)
        target_w = 500
        scale = target_w / W
        target_h = int(H * scale)
        frame_img = frame_img.resize((target_w, target_h), Image.Resampling.LANCZOS)
        
        # Convert to Adaptive Palette (8-bit color) for high-quality compact GIF
        frames.append(frame_img.convert("P", palette=Image.Palette.ADAPTIVE))
        
    # Save as animated looping GIF
    print(f"Saving compiled looping GIF to {OUTPUT_GIF}...", flush=True)
    frames[0].save(
        OUTPUT_GIF,
        save_all=True,
        append_images=frames[1:],
        duration=70,  # ~14 frames per second
        loop=0,
        optimize=True
    )
    print("Successfully created burning fire animation!")
    return True

if __name__ == "__main__":
    generate_seamless_fire_gif()

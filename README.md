# 🏛️ CBSE History Museum - Virtual Timeline Tour

[![Platform](https://img.shields.io/badge/platform-web-brightgreen.svg)](https://developer.mozilla.org/en-US/docs/Web)
[![Three.js](https://img.shields.io/badge/Three.js-r128-yellow.svg)](https://threejs.org/)

A comprehensive **3D Virtual Museum** and **Interactive Timeline** for CBSE Social Science History (Grades 6-10). Students can explore historical events through an immersive 3D robot-guided tour or a detailed chronological timeline view.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [Modes](#-modes)
- [Data Structure](#-data-structure)
- [Customization](#-customization)
- [File Structure](#-file-structure)
- [Browser Support](#-browser-support)
- [Troubleshooting](#-troubleshooting)
- [Educational Value](#-educational-value)
- [Contributing](#-contributing)

---

## 🎯 Overview

The **CBSE History Museum** is an interactive web application designed to help students visualize and understand historical timelines, cause-effect relationships, and key events from the CBSE Social Science curriculum (Grades 6-10).

### Key Highlights
- **📅 Historical Timeline View** (Default) - Chronological card-based layout
- **🎮 3D Virtual Museum Tour** - Robot-guided immersive experience
- **📖 382+ Subtopics** - Complete coverage of CBSE History syllabus
- **🔍 Search & Filter** - Find topics by grade, keyword, or era
- **📱 Responsive Design** - Works on desktops, tablets, and mobiles

---

## ✨ Features

### Timeline View (Default)
| Feature | Description |
|---------|-------------|
| Vertical Timeline | Alternating left/right cards with connecting line |
| Era Labels | Prehistory, Ancient India, Medieval, Mughal, Colonial, Nationalism, World History |
| Year Badges | Clear display of historical periods |
| Grade Filters | Filter by Grade 6, 7, 8, 9, or 10 |
| Search | Search by title, subtitle, or cause-effect text |
| Click-to-Expand | Modal dialog with complete details |
| Responsive | Works on all screen sizes |

### 3D Museum Tour
| Feature | Description |
|---------|-------------|
| Robot Guide | Animated robot walks to each panel |
| Human-like Walking | Legs swing, body faces direction, arms swing naturally |
| Pointing Animation | Robot points at panels while explaining |
| Third-person Camera | Follows robot from behind |
| Auto-navigation | Automatic tour through all panels |
| Controls | Start, Pause, Resume, Stop, Seek bar |
| Classroom Entry | Robot walks into side classrooms (7A, 10A) |

### Data Coverage
| Grade | Topics Covered |
|-------|----------------|
| Grade 6 | Prehistory, Indus Valley, Early Humans |
| Grade 7 | Medieval India, Rajputs, Cholas, Delhi Sultanate, Bhakti, Mughal Empire |
| Grade 8 | Colonial India, East India Company, Revolt of 1857, Social Reform |
| Grade 9 | French Revolution, Russian Revolution, Nazism, World History |
| Grade 10 | Indian Nationalism, Gandhian Movements, Partition, Global World |

---

## 🖥️ Demo

### Screenshots

**Timeline View (Default)**
```
┌─────────────────────────────────────────────────────────────┐
│  📅 Historical Timeline of Indian & World History           │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│     ●  📅 c. 1.7 million years ago                         │
│    ┌─────────────────────────────────────┐                 │
│    │ 🔥 Discovery of Fire                 │                 │
│    │ Cause: Environmental adaptation...   │                 │
│    └─────────────────────────────────────┘                 │
│                                                             │
│                     ●  📅 c. 2600 - 1900 BCE               │
│                    ┌─────────────────────────────────────┐ │
│                    │ 🏛️ Indus Valley Civilisation         │ │
│                    │ Cause: Surplus agriculture...        │ │
│                    └─────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

**3D Museum Tour**
```
┌─────────────────────────────────────────────────────────────┐
│  🤖 Robot Guide walking through museum                      │
│                                                             │
│         ┌─────┐                                            │
│         │ 🏛️ │ ← Panel                                     │
│         └─────┘                                            │
│            ↑                                               │
│         🤖 👈 Robot pointing                               │
│                                                             │
│  Controls: ▶ START | ⏸ PAUSE | ▶ RESUME | ⏹ STOP | ⏪══⏩  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Installation

### Option 1: Direct Download (Recommended)

1. Download the `index.html` file
2. Save it to your computer (e.g., Desktop)
3. Double-click to open in any modern web browser

### Option 2: Clone Repository

```bash
git clone https://github.com/yourusername/cbse-history-museum.git
cd cbse-history-museum
python -m http.server 8000
# OR use any local server
# Then open http://localhost:8000 in your browser
```

### Option 3: Host on School Server

1. Upload the `index.html` file to your school web server
2. Access via: `https://yourschool.edu/history-museum/`

### Requirements

- **No installation required** - Single HTML file
- **Internet connection** - For loading Three.js library (only for 3D mode)
- **Modern browser** - Chrome, Firefox, Edge, Safari (latest versions)

---

## 📖 Usage Guide

### Starting the Application

1. **Open** `index.html` in your web browser
2. **Default view** is the Historical Timeline

### Timeline View Controls

| Control | Action |
|---------|--------|
| 🔍 Search Box | Type keywords to filter topics |
| Grade Buttons | Click "Grade 6", "Grade 7", etc. to filter |
| 🔄 Reset | Clear all filters |
| ⬆ Top Button | Scroll to top of timeline |
| Click Card | Opens modal with complete details |

### 3D Museum Tour Controls

| Button | Function |
|--------|----------|
| ▶ START TOUR | Robot begins walking from first panel |
| ⏸ PAUSE | Freezes robot and auto-navigation |
| ▶ RESUME | Continues from paused position |
| ⏹ STOP | Ends tour, returns to idle |
| ⏪ Seek Bar | Drag to jump to any panel |
| 🖱️ Drag Mouse | Look around in 3D space |
| Click Panel | Show details (robot will point) |

### Keyboard Shortcuts (3D Mode only)

| Key | Action |
|-----|--------|
| Mouse Drag | Rotate camera |
| Scroll | Zoom in/out |

---

## 🎮 Modes

### Mode Switching

The application has two modes that can be switched at any time:

```
┌─────────────────────────────────────────────────────────────┐
│  🏛️ CBSE HISTORY MUSEUM    [📅 TIMELINE VIEW] [🎮 3D TOUR]  │
└─────────────────────────────────────────────────────────────┘
```

| Mode | Default | Best For |
|------|---------|----------|
| **Timeline View** | ✅ Yes | Quick browsing, exam preparation, printing |
| **3D Tour** | ❌ No | Immersive classroom presentation, engagement |

### Timeline View Details

- **Layout**: Vertical alternating timeline with connecting line
- **Eras**: Prehistory → Ancient → Medieval → Mughal → Colonial → Nationalism → World History
- **Cards show**: Year, Title, Subtitle, Grade, Location, Cause-Effect preview
- **Click**: Opens modal with complete information

### 3D Tour Details

- **Robot Guide**: Animated character with walking and pointing
- **Path**: Corridor (main timeline) + Classroom side rooms
- **Classrooms**: 
  - Classroom 7A - Mughal Empire (Grade 7 details)
  - Classroom 10A - Indian Nationalism (Grade 10 details)
- **Auto-navigation**: 5 seconds per panel, smooth transitions
- **Camera**: Third-person following robot

---

## 📊 Data Structure

The application contains **382 subtopics** organized as:

```json
{
  "grade": "6",
  "chapter_name": "Ch 6: The Beginnings of Indian Civilisation",
  "topic_name": "6.1 Indus Valley City Planning",
  "subtopic_name": "Grid patterns and streets at Harappa",
  "year_period": "c. 2600 BCE – 1900 BCE",
  "location": "Harappa and Mohenjo-Daro, Pakistan",
  "cause_effect": "Cause: Need for organized urban living...",
  "corridor_classroom_position": "Panel 3 – Position 1",
  "display_location": "Corridor"
}
```

### Data Coverage by Grade

| Grade | Number of Subtopics | Key Eras |
|-------|---------------------|----------|
| Grade 6 | ~50 | Prehistory, Indus Valley, Early Humans |
| Grade 7 | ~80 | Medieval India, Mughal Empire, Bhakti |
| Grade 8 | ~70 | Colonial India, Revolt of 1857, Social Reform |
| Grade 9 | ~60 | French Revolution, Russian Revolution, Nazism |
| Grade 10 | ~70 | Indian Nationalism, Gandhi, Partition |

---

## 🛠️ Customization

### Adding New Topics

Edit the `allTopics` array in the JavaScript section:

```javascript
const allTopics = [
  {
    id: 37,
    title: "Your New Topic",
    subtitle: "Brief description",
    year: "c. 1000 CE",
    era: "Your Era",
    causeEffect: "Cause: ... Effect: ...",
    location: "Main Corridor",
    grade: "Grade 7",
    color: "#ff9800"
  }
];
```

### Changing Colors

Modify the `color` property for each topic:

```javascript
color: "#ff9800"  // Orange
color: "#4caf50"  // Green
color: "#2196f3"  // Blue
color: "#e91e63"  // Pink
```

### Adding a New Classroom (3D Mode)

1. Add waypoint entries to the `waypoints` array
2. Define robot position `robotPos`
3. Set `facingAngle` for direction (0 = +X, π/2 = +Z, -π/2 = -Z)
4. Update the classroom floor visuals

### Changing Walking Speed

```javascript
let perPanelStayDuration = 5000;  // milliseconds (default 5 sec)
let walkDuration = 2500;          // milliseconds (default 2.5 sec)
```

---

## 📁 File Structure

```
cbse-history-museum/
│
├── index.html              # Main application file (single file)
│
├── README.md               # This documentation
│
└── assets/ (optional)      # Additional assets (if any)
    ├── images/
    └── data/
```

**Note:** The entire application is contained in a **single HTML file** for easy distribution.

---

## 🌐 Browser Support

| Browser | Version | Timeline View | 3D Mode |
|---------|---------|---------------|---------|
| Google Chrome | 90+ | ✅ Full | ✅ Full |
| Mozilla Firefox | 88+ | ✅ Full | ✅ Full |
| Microsoft Edge | 90+ | ✅ Full | ✅ Full |
| Safari | 14+ | ✅ Full | ✅ Full |
| Opera | 76+ | ✅ Full | ✅ Full |
| Chrome (Android) | 90+ | ✅ Full | ⚠️ May vary |
| Safari (iOS) | 14+ | ✅ Full | ⚠️ May vary |

**3D Mode Requirements:**
- WebGL support
- Graphics hardware (integrated GPU is sufficient)
- 4GB+ RAM recommended

---

## 🔧 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **3D mode doesn't load** | Check internet connection (Three.js CDN). Use Timeline View instead. |
| **Blank screen** | Clear browser cache, refresh page (Ctrl+F5) |
| **Robot not moving** | Click "START TOUR" button. Check console for errors (F12). |
| **Slow performance** | Close other tabs. Use Timeline View on older computers. |
| **Text overlapping** | Zoom out (Ctrl + -) or refresh page |
| **Mobile issues** | Use Timeline View (3D mode requires more resources) |

### Console Debugging

Open Developer Tools (F12) and check for:

```
No errors expected. Expected console message:
"CBSE History Museum - Ready"
"3D Mode loaded successfully" (when switching to 3D)
```

### Performance Tips

1. **For older computers:** Use Timeline View only
2. **For classroom projectors:** Switch to Timeline View (better readability)
3. **For individual study:** Timeline View is faster and easier to browse
4. **For engagement:** 3D Mode works best on modern laptops

---

## 📚 Educational Value

### Learning Outcomes

| Skill | How It's Addressed |
|-------|---------------------|
| Chronological Thinking | Timeline view shows events in order |
| Cause & Effect | Each card explains causes and effects |
| Historical Empathy | 3D immersion creates engagement |
| Information Retrieval | Search and filter functions |
| Visual Learning | Color-coded eras and card layouts |
| Self-paced Learning | Manual navigation allows control |

### Curriculum Alignment

- **CBSE Class 6:** Our Pasts-I (Chapters 1-6)
- **CBSE Class 7:** Our Pasts-II (Chapters 1-10)
- **CBSE Class 8:** Our Pasts-III (Chapters 1-8)
- **CBSE Class 9:** India and Contemporary World-I
- **CBSE Class 10:** India and Contemporary World-II

### Classroom Activities

| Activity | Suggested Mode | Duration |
|----------|----------------|----------|
| Introduce new chapter | Timeline View | 10 min |
| Review before exam | Timeline View + Search | 20 min |
| Engage students | 3D Tour | 15 min |
| Group project research | Timeline View | 30 min |
| Cause-effect analysis | Timeline View + Click modal | 15 min |

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing`)
3. **Commit** changes (`git commit -m 'Add amazing feature'`)
4. **Push** to branch (`git push origin feature/amazing`)
5. **Open** a Pull Request

### Contribution Areas

- Adding more historical topics
- Improving 3D robot animations
- Adding audio narration
- Translating to other languages
- Adding quiz/assessment features

---

## 🙏 Acknowledgements

- **NCERT** - For the CBSE curriculum framework
- **Three.js** - For the 3D graphics library
- **CBSE** - For the Social Science syllabus
- **Open Source Community** - For inspiration and tools

---

## 📞 Contact & Support

| Issue Type | Contact |
|------------|---------|
| Bug Reports | Open GitHub Issue |
| Feature Requests | Open GitHub Issue |
| General Questions | School IT Department |
| Content Corrections | Subject Teacher |

---

## 📝 Changelog

### Version 2.0 (Current)
- ✅ Added 3D robot-guided tour
- ✅ Added Timeline View as default
- ✅ Added search and filter functionality
- ✅ Added classroom entry/exit animations
- ✅ Added 382 subtopics covering grades 6-10
- ✅ Added responsive design for mobile

### Version 1.0 (Initial)
- Basic timeline view
- Grade-wise filtering
- Cause-effect explanations

---

## 🎓 Teacher Quick Start Guide

### 5 Minutes to Start

1. **Download** `index.html` to your computer
2. **Open** in Chrome or Firefox
3. **Project** on classroom screen
4. **Click** "START TOUR" for 3D mode OR browse Timeline View

### Lesson Plan Suggestion

```
1. (2 min) Open Timeline View, show All Grades
2. (5 min) Search for specific topic (e.g., "Indus Valley")
3. (5 min) Click cards to show cause-effect
4. (8 min) Switch to 3D Tour, let robot guide
5. (5 min) Q&A using modal details
```

---

## 🧑‍🎓 Student Quick Guide

### Finding Information

1. **Browse** the timeline cards
2. **Filter** by your grade using buttons
3. **Search** for specific words
4. **Click** any card for full details

### Studying for Exams

1. Use **Grade filter** to focus on your syllabus
2. Note **Cause & Effect** from each card
3. Use **Year badges** for chronology
4. Switch to **3D Tour** for visual memory

---

## 🔮 Future Roadmap

- [ ] Audio narration for each subtopic
- [ ] Quiz mode with multiple-choice questions
- [ ] Student progress tracking
- [ ] Downloadable PDF notes
- [ ] Mobile app version (PWA)
- [ ] More languages (Hindi, Tamil, Telugu)
- [ ] VR headset support

---

**Made with ❤️ for CBSE Students and Teachers**

*Last Updated: June 2024*
```

This README.md provides complete documentation covering:
- Installation and setup
- Usage instructions for both modes
- Troubleshooting common issues
- Customization options
- Educational value and lesson plans
- Technical specifications
- Browser compatibility
- Quick start guides for teachers and students
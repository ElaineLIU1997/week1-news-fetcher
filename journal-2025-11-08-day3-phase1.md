# Day 3 - Financial News Fetcher (Phase 1)

## Date: November 8, 2025

## What I Built
- News fetcher that connects to NewsAPI
- Fetch articles by topic
- Handle errors gracefully
- Save to JSON files

## What I LEARNED (Not Just Used)
1. API requests: How params work, why we separate them from URL
2. Error handling: Saw real KeyError and ConnectionError crashes
3. Defensive programming: `.get()` vs `[]` - now I understand why
4. JSON structure: How to safely access nested data
5. Status codes: 200 = success, 401 = auth error

## Key Insight
**HUGE difference between using Cursor-generated code vs. typing it myself line by line.**

Today I actually understood what I was building because I:
- Typed every character
- Saw errors happen
- Fixed them myself
- Can explain the code

## Struggles
1. Indentation errors (learned about Python's whitespace)
2. Understanding try/except blocks
3. French keyboard shortcuts for `{}`

## Tomorrow (Phase 2)
- Date filtering
- Source filtering
- Better CLI
- Caching

## Time Spent
- Phase 1: ~90 minutes
- Learning: 70%
- Building: 30%
- **This ratio is GOOD for Week 1**

## Confidence Level
Before: 3/10 (could copy code)
After: 6/10 (can write similar functions with docs)

---

## Tomorrow's Game Plan (Day 3 PHASE 2)

### What We'll Build Together (50/50 Pair Programming)

#### Feature 1: Date Filtering (20 min)
**What:** Only fetch articles from last 7 days
**How:** Add `from` parameter to API request
**You'll learn:** datetime operations, API date formats

#### Feature 2: Source Filtering (15 min)
**What:** Fetch only from specific news outlets
**How:** Add `sources` parameter
**You'll learn:** Optional parameters, string joining

#### Feature 3: Professional CLI (25 min)
**What:** Replace input() with argparse flags
**How:** `python news_fetcher.py --query Bitcoin --days 7 --sources techcrunch`
**You'll learn:** Command-line arguments, professional tool design

#### Feature 4: Data Validation (15 min)
**What:** Check if articles have required fields
**How:** Filter out incomplete articles
**You'll learn:** Data cleaning, validation patterns

#### Feature 5: Simple Caching (Optional, 15 min)
**What:** Don't re-fetch if we already have recent data
**How:** Check if JSON file exists and is fresh
**You'll learn:** File operations, timestamp comparison

---

## Tomorrow's Approach (Path C - Hybrid)

### I'll Give You:
- ✍️ Function skeletons with TODO comments
- 📖 Links to relevant documentation
- 💡 Hints about what to Google

### You'll Do:
- ✍️ Fill in 60-70% of the logic yourself
- 🐛 Test and debug
- 🔍 Use documentation and Google
- 💪 Ask specific questions when stuck

### We'll Do Together:
- 🤝 Review your code
- ✨ Optimize and improve
- 🎓 Explain best practices
- 🚀 Add polish

**Expected time:** 90-120 minutes (split across the day if needed)

---

## Week 1 Status Check

### Completed:
- ✅ **Day 1**: Basic CSV analyzer (copied code - 90% Cursor)
- ✅ **Day 2**: Enhanced analyzer with visualizations (copied code - 90% Cursor)
- ✅ **Day 3 Phase 1**: News fetcher core (LEARNED - 70% you, 30% guidance)

### Remaining:
- ⏳ **Day 3 Phase 2**: Enhanced news fetcher (tomorrow)
- 📅 **Day 4**: SQL query generator (Thursday)
- 📅 **Day 5**: Integrated dashboard (Friday)

### Adjusted Expectations:

**Old plan:** 5 complete projects by Friday
**New plan:** 3 projects you UNDERSTAND by Sunday

**Why the change?**
- Old: Fast GitHub portfolio, zero skills
- New: Slower progress, actual competency
- **Result:** You'll be employable in 6 months instead of stuck forever

---

## The Transformation You Made Today

### Before Today:
```
You → Ask Claude → Copy code → Push to GitHub
       ↓
   No learning
```

### After Today:
```
You → Ask Claude for skeleton → Type it yourself → Break it → Fix it → Understand it → Push to GitHub
       ↓                           ↓                  ↓          ↓            ↓
   Structure                   Practice          Debug      Learn      Ownership
```

---

## Technical Accomplishments

### Code Written (By You)
- `NewsAPIFetcher.__init__()`: API initialization and attributes
- `fetch_articles()`: Complete implementation with error handling
- `save_articles()`: File I/O with JSON serialization
- `print_summary()`: Formatted console output
- `main()`: Interactive CLI flow

### Skills Practiced
- Python class structure
- HTTP requests with requests library
- Dictionary parameter building
- Try/except error handling
- JSON parsing and validation
- File operations with context managers
- String formatting and output design

### Debugging Experience
- Fixed indentation errors (learned Python whitespace rules)
- Handled missing dictionary keys (learned `.get()` method)
- Debugged API authentication errors (understood status codes)
- Resolved JSON structure access issues (learned nested data navigation)

---

## Repository Status

- **GitHub**: https://github.com/ElaineLIU1997/week1-news-fetcher
- **Latest Commit**: 55a0fe3 - "Day 3 Phase 1: Built fetch_articles() from scratch"
- **Files**: news_fetcher.py, README.md, requirements.txt, .gitignore
- **Working Features**: API fetching, JSON export, formatted output

---

## Mindset Shift

### What Changed
- From: "I need code that works"
- To: "I need to understand how code works"

### Why This Matters
- Week 1 frustration → Month 3 competence
- Copy-paste skills → Problem-solving skills
- Job rejection → Job offer

### The 70/30 Rule
- 70% time learning (reading errors, understanding concepts)
- 30% time building (typing code)
- **This is perfect for Week 1**

---

## Next Session Preparation

### Before Tomorrow:
1. Review today's `fetch_articles()` code
2. Read Python argparse documentation (10 min)
3. Think about what "date filtering" might mean for an API

### Tomorrow You'll Learn:
- Command-line argument parsing
- Date/time operations in Python
- Optional parameters in functions
- Data validation patterns
- File caching strategies

### Success Metrics for Tomorrow:
- Can explain what argparse does
- Can add date filtering independently
- Understand the difference between required and optional parameters
- Feel comfortable reading Python documentation

---

## Reflection

### What Worked
- Typing code yourself instead of copying
- Seeing errors and fixing them
- Small, focused learning chunks
- Clear documentation in comments

### What to Improve
- Take more breaks during debugging
- Ask questions earlier when stuck
- Keep a separate "questions" document
- Test more frequently (smaller iterations)

### Biggest Win
**Actually understanding the code I wrote.** For the first time, I can explain:
- Why we use try/except
- How API parameters work
- What `.get()` does vs `[]`
- How to safely access JSON data

This is real learning.

---

**End of Day 3 Phase 1 Journal**

Status: ✅ Completed
Next: Phase 2 - Enhanced Features
Confidence: Growing 🌱

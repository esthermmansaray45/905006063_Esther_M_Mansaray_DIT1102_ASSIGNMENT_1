# PROG211 Assignment: Digital Student Learning Portal System

## Group Members & Team Details
- **Module:** Object-Oriented Programming 1 (PROG211)[cite: 1]
- **Institution:** Limkokwing University of Creative Technology (Sierra Leone)[cite: 1]
- **Lecturer:** Amandus Benjamin Coker[cite: 1]

## Project Overview
This project builds a real-world **Education Domain** solution—a Digital Student Learning Portal System—utilizing core Object-Oriented Programming (OOP) concepts from Lectures 1 through 3[cite: 2, 3].

## How the Code Meets Assignment Tasks
1. **Task 1 (OOP Basics):** Implements three core classes (`Student`, `Course`, and `LearningPortal`) featuring attributes, instance methods (`display_info`, `update_major`), object creation, and cross-object interaction (`enroll_interaction`)[cite: 2, 3].
2. **Task 2 (Data Structures):** Uses a **Python Dictionary** (`student_registry`) to store and look up multiple student objects using their unique ID as keys, alongside explicit functions to add and display data. It also implements **Tuples** for immutable course metadata (credits and semester) to claim eligibility for bonus marks.
3. **Task 3 (Methods & DPG):** Features instance methods, class methods (`@classmethod` via `get_institution_summary`), and structured clean code[cite: 3].

## Digital Public Goods (DPG) Standards Alignment
This project aligns with DPG core principles:
- **Open-Source:** Hosted publicly on GitHub under an open license[cite: 2].
- **Inclusive & Accessible Design:** Designed with a lightweight terminal text interface that can run on low-spec hardware or simple Python environments.
- **Privacy-Respecting:** Uses generic student identification numbers and avoids storing vulnerable, sensitive personal records[cite: 2].
- **Modular & Reusable:** Code is cleanly separated into distinct, specialized classes (`Student`, `Course`, `LearningPortal`), making it easy to extend or scale.
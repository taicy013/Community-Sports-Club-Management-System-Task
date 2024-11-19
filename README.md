## **Project: Community Sports Club Management System**

### **Objective**  
Design a system to manage a sports club, involving members, coaches, and staff. This task focuses on using inheritance, composition, and object interaction while demonstrating relationships and behaviours unique to each class.

---

### **Step 1: Define the Base Class**

### **1. Person Class**  
A base class for all individuals in the sports club.

**Attributes**:  
- `name`: Full name of the person.  
- `age`: The age of the person.  
- `contact_number`: The person's contact number.  

**Methods**:  
- `set_details(name, age, contact_number)`: Sets the person's details.  
- `get_details()`: Returns a string summarising the person's details:  
  `"Name: [name], Age: [age], Contact Number: [contact_number]"`.

---

### **Step 2: Define Subclasses**

### **2. Member Class (inherits from Person)**  
A class representing club members who participate in sports activities.

**Attributes**:  
- Inherits all attributes from `Person`.  
- `membership_id`: A unique ID for the member (e.g., "M3456").  
- `sport`: The sport they are enrolled in (e.g., "Football").  
- `performance_scores`: A list of scores reflecting their performance.  

**Methods**:  
- `set_member_details(membership_id, sport)`: Sets the member's ID and sport.  
- `add_performance_score(score)`: Adds a score to the member’s `performance_scores`.  
- `calculate_average_score()`: Calculates and returns the average score if there are scores; otherwise, returns 0.  
- `get_member_summary()`: Returns the member’s details, including their average performance score.  

---

### **3. Coach Class (inherits from Person)**  
A class representing the coaches who train members.

**Attributes**:  
- Inherits all attributes from `Person`.  
- `coach_id`: A unique ID for the coach (e.g., "C1234").  
- `specialisation`: The sport they coach (e.g., "Tennis").  
- `salary`: The coach's salary.  
- `mentees`: A list of `Member` objects representing their mentees (starts as an empty list).  

**Methods**:  
- `set_coach_details(coach_id, specialisation, salary)`: Sets the coach’s details.  
- `assign_mentee(member)`: Accepts a `Member` object, adds them to the `mentees` list, and prints:  
  `"Coach [coach_name] is now mentoring [member_name] in [member_sport]."`  
- `get_mentees()`: Returns a list of names and sports of all the coach’s mentees.  
- `increase_salary(percentage)`: Increases the coach’s salary by a given percentage.  

---

### **4. Staff Class (inherits from Person)**  
A class representing administrative staff who manage the club.

**Attributes**:  
- Inherits all attributes from `Person`.  
- `staff_id`: A unique ID for the staff member (e.g., "S4567").  
- `position`: Their job role (e.g., "Club Secretary").  
- `years_of_service`: The number of years they have worked at the club.  

**Methods**:  
- `set_staff_details(staff_id, position, years_of_service)`: Sets the staff member’s details.  
- `increment_years_of_service()`: Increases the `years_of_service` by 1.  
- `assist_member(member)`: Accepts a `Member` object and prints:  
  `"Staff [staff_name] assisted [member_name] in resolving an issue."`  
- `get_staff_summary()`: Returns the staff member’s details, including years of service.  

---

### **Step 3: Create and Use the Classes**

1. **Create Objects**  
   - Create 2 `Member` objects.  
   - Create 2 `Coach` objects.  
   - Create 1 `Staff` object.  

2. **Demonstrate Functionality**  
   - Assign a member to a coach using `assign_mentee`.  
   - Add performance scores for a member and calculate their average score.  
   - Use a staff member to assist a member.  
   - Increase a coach's salary by 15%.  
   - Increment a staff member’s years of service.  

3. **Output**  
   - Print the summaries for all objects, showing their updated details.

---

### **Extension Task (Harder)**

**Scenario**: Develop a mentorship programme for coaches.  

1. Add a `mentorship_group` attribute to the `Coach` class, which is a list of `Coach` objects that they are mentoring (starts as an empty list).  

2. Add a `mentor_coach(coach)` method in the `Coach` class that:  
   - Accepts another `Coach` object and adds them to the `mentorship_group`.  
   - Prints:  
     `"Coach [coach_name] is now mentoring Coach [mentee_coach_name] in [mentee_specialisation]."`

3. Add a `get_mentorship_group()` method in the `Coach` class that:  
   - Returns a list of names and specialisations of the coaches in the `mentorship_group`.  

**Challenge**: Make coaches simultaneously mentor members and other coaches while maintaining clear relationships.  

**Example Output**:  
```python
coach1.mentor_coach(coach2)
coach1.assign_mentee(member1)

# Output
# Coach Alex is now mentoring Coach Beth in Football.
# Coach Alex is now mentoring Member John in Football.

coach1.get_mentorship_group()  # Returns: ["Beth (Football)"]
coach1.get_mentees()  # Returns: ["John (Football)"]
```

class person:
    def __init__(self,name,age,number,p_id):
        self.name = name.lower()
        self.age = age
        self.number = number
        self.p_id = p_id

    def set_details(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.number = input("Enter phone number: ")
    def get_details(self):
        print("------%s's DETAILS------" %(self.name))
        print("AGE: ", self.age)
        print("CONTACT NUMBER: ", self.number)

class member(person):
    def __init__(self,name,age,number,p_id,sport,scores):
        super().__init__(name,age,number,p_id)
        self.sport = sport
        self.scores = scores

    def set_m_details(self):
        self.p_id = input("Enter your member ID: ")
        self.sport = input("Enter your sport: ")
    def add_scores(self):
        quit = ''
        while quit != 'q':
            user = input("Enter your score (or type 'q' to quit): ")
            if user.lower() == 'q':
                quit = 'q'
            else:
                self.scores.append(int(user))
    def avg(self):
        return round(sum(self.scores)/len(self.scores))
    def get_details(self):
        super().get_details()
        print("MEMBER ID: ", self.p_id)
        print("SPORT: ", self.sport)
        print("AVG SCORE: ", self.avg())

class coach(person):
    def __init__(self,name,age,number,p_id,special,pay,mentees):
        super().__init__(name,age,number,p_id)
        self.special = special
        self.pay = pay
        self.mentees = {name:name.sport for name in mentees}
    
    def set_c_details(self):
        self.p_id = input("Enter your coach ID: ")
        self.special = input("Enter your specialisation: ")
        self.pay = int(input("Enter your salary: "))
    def add_mentees(self):
        quit = ''
        while quit != 'q':
            user = input("Enter the name of your mentee (or type 'q' to quit): ").lower()
            if user == 'q':
                quit = 'q'
            else:
                self.mentees[user.lower()] = user.sport
                print(" Coach {self.name} is now mentoring {user.name} in {user.sport}")
    def get_mentees(self):
        print("------{self.name}'s MENTEES------")
        print(self.mentees)
    def increase_pay(self,p):
        self.pay *= 1 + (p/100)
        return "{self.name}'s PAY HAS INCREASED TO {self.pay}"

class staff(person):
    def __init__(self,name,age,number,p_id,pos,exp):
        super().__init__(name,age,number,p_id)
        self.pos = pos
        self.exp = int(exp)

    def set_s_details(self):
        self.p_id = input("Enter your staff ID: ")
        self.pos = input("Enter your position: ")
        self.exp = int(input("Enter your years of service: "))
    def get_details(self):
        super().get_details()
        print("STAFF ID: ", self.p_id)
        print("POSITION: ", self.pos)
        print("YEARS OF SERVICE: ", self.exp)
    def years_increase(self):
        self.exp += 1
        return "{self.name}'s YEARS OF SERVICE HAS INCREASED TO {self.exp}"

member1 = member("Taco",21,'072832849348','ieouoiwru')
member2 = member("blue",22,'03483274823','heoiwuiurow')

coach1 = coach("krabb",34,'289798274982','ewoeirdsn')

    
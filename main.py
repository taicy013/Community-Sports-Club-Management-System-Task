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
        return "AVG SCORE: ", round(sum(self.scores)/len(self.scores))
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
        self.mentees = mentees
    
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
                sport = input("Enter member's sport: ")
                self.mentees[user.lower()] = sport
                print("Coach %s is now mentoring %s in %s" %(self.name,user,sport))
    def get_mentees(self):
        print("------%s's MENTEES------" %(self.name))
        print(self.mentees)
    def increase_pay(self,p):
        self.pay *= 1 + (p/100)
        return "%s's PAY HAS INCREASED TO %d" %(self.name,self.pay)
    def get_details(self):
        super().get_details()
        print("COACH ID: ", self.p_id)
        print("SPECIALISATION: ", self.special)
        print("PAY: ", self.pay)
        print("MENTEES: ", self.mentees)

class staff(person):
    def __init__(self,name,age,number,p_id,pos,exp):
        super().__init__(name,age,number,p_id)
        self.pos = pos
        self.exp = int(exp)

    def set_s_details(self):
        self.p_id = input("Enter your staff ID: ")
        self.pos = input("Enter your position: ")
        self.exp = int(input("Enter your years of service: "))
    def years_increase(self):
        self.exp += 1
        return "%s's YEARS OF SERVICE HAS INCREASED TO %d" %(self.name,self.exp)
    def assist(self,m):
        return "STAFF %s ASSISSTED %s IN RESOLVING AN ISSUE" %(self.name,m.name)
    def get_details(self):
        super().get_details()
        print("STAFF ID: ", self.p_id)
        print("POSITION: ", self.pos)
        print("YEARS OF SERVICE: ", self.exp)

member1 = member("Taco",21,'072832849348','ieouoiwru',"football",[4,3,2,5,7])
member2 = member("blue",22,'03483274823','heoiwuiurow','tennis',[5,4,7,12,3])

coach1 = coach("krabb",34,'289798274982','ewoeirdsn','tennis',150000,{member2.name:member2.sport})
coach2 = coach("Sponge",25,'289798313212','esrewejkrh','football',160000,{member1.name:member1.sport})

staff1 = staff("squid",54,'9304820374','lerherhow','receptionist',15)

coach1.add_mentees()
coach1.get_details()

member2.add_scores()
print(member2.avg())
member2.get_details()

print(staff1.assist(member1))
print(staff1.years_increase())
staff1.get_details()

print(coach2.increase_pay(15))
coach2.get_details()

    
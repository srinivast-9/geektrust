import sys

_MALE_ = 'male'
_FEMALE_ = 'female'

class Person:
    by_name = {}
    def __init__(self, name, gender, ishead=False, level=0):
        self.name = name
        self.gender = gender
        self.level = level
        self.ishead = ishead
        self.father = ''
        self.mother = ''
        self.spouse = ''
        self.brothers = []
        self.sisters = []
        self.sons = []
        self.daughters = []
        self.slaws = []
        self.blaws = []
        self.puncles = []
        self.muncles = []
        self.paunts = []
        self.maunts = []
        self.by_name[self.name] = self

    def add_child(self,child):
        if self.gender == _FEMALE_ and self.spouse != '' and child.level == 0 and not child.ishead:
            family = Person.by_name.values()
            child.level = self.level + 1
            child.father = self.spouse
            child.mother = self.name
            child.muncles = self.brothers
            child.maunts = self.sisters
            child.puncles = self.blaws
            child.paunts = self.slaws

            for person in family:
                for name in self.sons+self.daughters:
                    if name == person.name:
                        if person.gender == _MALE_:
                            child.brothers.append(person.name)
                            if person.spouse != '':
                                child.slaws.append(person.spouse)
                        else:
                            child.sisters.append(person.name)
                            if person.spouse != '':
                                child.blaws.append(person.spouse)
                        if child.gender == _MALE_:
                            person.brothers.append(child.name)
                        else:
                            person.sisters.append(child.name)
                        break
                    elif name == person.spouse:
                        if child.gender == _MALE_:
                            person.blaws.append(child.name)
                        else:
                            person.slaws.append(child.name)
                        break

            if child.gender == _MALE_:
                self.sons.append(child.name)
            else:
                self.daughters.append(child.name)

            for person in family:
                if self.spouse == person.name:
                    child.puncles = person.brothers
                    child.paunts = person.sisters
                    person.sons = self.sons
                    person.daughters = self.daughters
                    break

            return True
        else:
            return False

    def add_spouse(self,spouse):
        family = Person.by_name.values()
        if self.gender != spouse.gender and self.spouse=='' and spouse.spouse == '':
            if spouse.level == 0 and self.level != 0:
                spouse.level = self.level
            elif spouse.level != 0 and self.level == 0:
                self.level = spouse.level

            spouse.spouse = self.name
            spouse.slaws = self.sisters
            spouse.blaws = self.brothers
            spouse.sons = self.sons
            spouse.daughters = self.daughters
            self.spouse = spouse.name
            self.slaws = spouse.sisters
            self.blaws = spouse.brothers

            for person in family:
                for name in self.brothers+self.sisters:
                    if name == person.spouse:
                        if person.gender == _MALE_:
                            self.blaws.append(person.name)
                            spouse.blaws.append(person.name)
                            if person.spouse != '':
                                spouse.slaws.append(person.spouse)
                        else:
                            self.slaws.append(person.name)
                            spouse.slaws.append(person.name)
                            if person.spouse != '':
                                spouse.blaws.append(person.spouse)

                        if self.gender == _MALE_:
                            person.blaws.append(self.name)
                            person.slaws.append(self.spouse)
                        else:
                            person.slaws.append(self.name)
                            person.blaws.append(self.spouse)
                        break

                for name in spouse.brothers+spouse.sisters:
                    if name == person.spouse:
                        if person.gender == _MALE_:
                            spouse.blaws.append(person.name)
                            self.blaws.append(person.name)
                            if person.spouse != '' :
                                spouse.slaws.append(person.spouse)
                        else:
                            spouse.slaws.append(person.name)
                            self.slaws.append(person.name)
                            if person.spouse != '':
                                spouse.blaws.append(person.spouse)

                        if spouse.gender == _MALE_:
                            person.blaws.append(spouse.name)
                            person.slaws.append(spouse.spouse)
                        else:
                            person.slaws.append(spouse.name)
                            person.blaws.append(spouse.spouse)
                        break


                for name in self.brothers+self.sisters:
                    if name == person.name:
                        if spouse.gender == _MALE_:
                            person.blaws.append(spouse.name)
                        else:
                            person.slaws.append(spouse.name)

                        if person.gender == _MALE_:
                            spouse.blaws.append(person.name)
                            if person.spouse != '':
                                self.slaws.append(person.spouse)
                        else:
                            spouse.slaws.append(person.name)
                            if person.spouse != '':
                                self.blaws.append(person.spouse)
                        break


                for name in spouse.brothers + spouse.sisters:
                    if name == person.name:
                        if self.gender == _MALE_:
                            person.blaws.append(self.name)
                        else:
                            person.slaws.append(self.name)

                        if person.gender == _MALE_:
                            self.blaws.append(person.name)
                            if person.spouse != '' :
                                spouse.slaws.append(person.spouse)
                        else:
                            self.slaws.append(person.name)
                            if person.spouse != '':
                                spouse.blaws.append(person.spouse)
                        break
            return True
        else:
            return False

def createFamilytree():
    shan = Person('King Shan',_MALE_,ishead=True)
    anga = Person('Queen Anga',_FEMALE_,ishead=True)
    anga.add_spouse(shan)
    chit = Person('Chit',_MALE_)
    ish = Person('Ish',_MALE_)
    vich = Person('Vich',_MALE_)
    aras = Person('Aras',_MALE_)
    satya = Person('Satya',_FEMALE_)
    anga.add_child(chit)
    anga.add_child(ish)
    anga.add_child(vich)
    anga.add_child(aras)
    anga.add_child(satya)

    amba = Person('Amba',_FEMALE_)
    amba.add_spouse(chit)
    dritha = Person('Dritha',_FEMALE_)
    tritha = Person('Tritha',_FEMALE_)
    vritha = Person('Vritha',_MALE_)
    amba.add_child(dritha)
    amba.add_child(tritha)
    amba.add_child(vritha)

    jaya = Person('Jaya',_MALE_)
    dritha.add_spouse(jaya)
    yodhan = Person('Yodhan',_MALE_)
    dritha.add_child(yodhan)

    lika = Person('Lika',_FEMALE_)
    lika.add_spouse(vich)
    vila = Person('Vila',_FEMALE_)
    chika = Person('Chika',_FEMALE_)
    lika.add_child(vila)
    lika.add_child(chika)

    chitra = Person('Chitra',_FEMALE_)
    chitra.add_spouse(aras)
    jnki = Person('Jnki',_FEMALE_)
    ahit = Person('Ahit',_MALE_)
    chitra.add_child(jnki)
    chitra.add_child(ahit)

    arit = Person('Arit',_MALE_)
    jnki.add_spouse(arit)
    laki = Person('Laki',_MALE_)
    lavnya = Person('Lavnya',_FEMALE_)
    jnki.add_child(laki)
    jnki.add_child(lavnya)

    vyan = Person('Vyan',_MALE_)
    satya.add_spouse(vyan)
    asva = Person('Asva',_MALE_)
    vyas = Person('Vyas',_MALE_)
    atya = Person('Atya',_FEMALE_)
    satya.add_child(asva)
    satya.add_child(vyas)
    satya.add_child(atya)

    satvy = Person('Satvy',_FEMALE_)
    satvy.add_spouse(asva)
    vasa = Person('Vasa',_MALE_)
    satvy.add_child(vasa)

    krpi = Person('Krpi',_FEMALE_)
    krpi.add_spouse(vyas)
    kriya = Person('Kriya',_MALE_)
    krithi = Person('Krithi',_FEMALE_)
    krpi.add_child(kriya)
    krpi.add_child(krithi)


if __name__ == '__main__':
    createFamilytree()
    family = Person.by_name.values()

    try:
        if len(sys.argv)<2:
            print('No test file location given as argument.')
            sys.exit(1)

        with open(sys.argv[1],'r') as f:
            for line in f.readlines():
                if line != '' and line != '\n':
                    command = line.strip('\n').split(' ')

                if command[0].lower() == 'add_child' and len(command)==4:
                    child = Person(command[2],command[3].lower())
                    for person in family:
                        if person.name == command[1]:
                            if person.add_child(child):
                                print('CHILD_ADDITION_SUCCEEDED')
                            else:
                                print('CHILD_ADDITION_FAILED')
                            break
                    else:
                        print('PERSON_NOT_FOUND')

                elif command[0].lower() == 'get_relationship' and len(command)==3:
                    for person in family:
                        if person.name == command[1]:
                            relationship = command[2].lower()
                            pstring = ''
                            if relationship == 'paternal-uncle':
                                if person.puncles:
                                    for puncle in set(person.puncles):
                                        pstring += puncle + ' '
                                else:
                                    pstring = 'NONE'
                            elif relationship == 'maternal-uncle':
                                if person.muncles:
                                    for muncle in set(person.muncles):
                                        pstring += muncle + ' '
                                else:
                                    pstring = 'NONE'
                            elif relationship == 'paternal-aunt':
                                if person.paunts:
                                    for paunt in set(person.paunts):
                                        pstring += paunt + ' '
                                else:
                                    pstring = 'NONE'
                            elif relationship == 'maternal-aunt':
                                if person.maunts:
                                    for maunt in set(person.maunts):
                                        pstring += maunt + ' '
                                else:
                                    pstring = 'NONE'
                            elif relationship == 'sister-in-law':
                                if person.slaws:
                                    for slaw in set(person.slaws):
                                        pstring += slaw + ' '
                                else:
                                    pstring = 'NONE'
                            elif relationship == 'brother-in-law':
                                if person.blaws:
                                    for blaw in set(person.blaws):
                                        pstring = blaw + ' '
                                else:
                                    pstring = 'NONE'
                            elif relationship == 'son':
                                if person.sons:
                                    for son in set(person.sons):
                                        pstring += son + ' '
                                else:
                                    pstring = 'NONE'
                            elif relationship == 'daughter':
                                if person.daughters:
                                    for daughter in set(person.daughters):
                                        pstring += daughter + ' '
                                else:
                                    pstring = 'NONE'
                            elif relationship == 'siblings':
                                siblings = person.brothers+person.sisters
                                if siblings:
                                    for sibling in set(siblings):
                                        pstring += sibling + ' '
                                else:
                                    pstring = 'NONE'
                            print(pstring)
                            break
                    else:
                        print('PERSON_NOT_FOUND')
                else:
                    print('PERSON_NOT_FOUND')
    except Exception as e:
        print(e)
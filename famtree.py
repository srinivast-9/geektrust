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
            child.brothers = self.sons
            child.sisters = self.daughters
            child.muncles = self.brothers
            child.maunts = self.sisters

            if child.gender == _MALE_:
                self.sons.append(child.name)
            else:
                self.daughters.append(child.name)
            '''
            for name in child.brothers:
                for person in family:
                    if name == person.name:
                        child.slaws.append(person.spouse)
                        break
            for name in child.sisters:
                for person in family:
                    if name == person.name:
                        child.blaws.append(person.spouse)
                        break
            for person in family:
                if self.spouse == person.name:
                    child.puncles = person.brothers
                    child.paunts = person.sisters
                    person.sons = self.sons
                    person.daughters = self.daughters
                    break
            '''
            for person in family:
                for name in child.brothers:
                    if name == person.name:
                        child.slaws.append(person.spouse)
                        break
                for name in child.sisters:
                    if name == person.name:
                        child.blaws.append(person.spouse)
                        break

            for person in family:
                if self.spouse == person.name:
                    child.puncles = person.brothers
                    child.paunts = person.sisters
                    person.sons = self.sons
                    person.daughters = self.daughters
                    break

            #print('CHILD_ADDITION_SUCCEEDED')
            return True
        else:
            #print('CHILD_ADDITION_FAILED')
            return False

    def add_spouse(self,spouse):
        if self.gender != spouse.gender and self.spouse=='' and spouse.spouse == '':
            spouse.level = self.level
            self.spouse = spouse.name
            spouse.spouse = self.name
            spouse.slaws += self.sisters
            spouse.blaws += self.brothers
            spouse.sons = self.sons
            spouse.daughters = self.daughters

            #print('SPOUSE_ADDITION_SUCCEEDED')
            return True
        else:
            #print('SPOUSE_ADDITION_FAILED')
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

    aria = Person('Aria',_FEMALE_)
    if chitra.add_child(aria):
        print('CHILD_ADDITION_SUCCEEDED')

    print(lavnya.maunts)
    print(aria.brothers+aria.sisters)
    #for p in family:
        #print(p.name)

if __name__ == '__main__':
    createFamilytree()
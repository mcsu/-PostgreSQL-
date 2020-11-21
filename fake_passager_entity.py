class FakePassager:
    # def __init__(self, paperstype, papersnumber, nationality, name, gender, birthdate, birthplace):
    #     self.paperstype = paperstype;
    #     self.papersnumber = papersnumber;
    #     self.nationality = nationality;
    #     self.name = name;
    #     self.gender = gender;
    #     self.birthdate = birthdate;
    #     self.birthplace = birthplace;

    def __init__(self):
        self.paperstype = ''
        self.papersnumber = ''
        self.nationality = ''
        self.name = ''
        self.gender = ''
        self.birthdate = ''
        self.birthplace = ''

    def __str__(self):
        result = 'passport_type：%s passport_number：%s nationality：%s name：%s gender：%s birth_date：' \
                 '%s birth_place：%s' %(self.paperstype, self.papersnumber, self.nationality, self.name,
                                      self.gender, self.birthdate, self.birthplace, )
        return result





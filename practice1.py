class convert:
    roman = ("i" , "ii" , "iii" , "iv" , "v" , "vi" , "vii" , "viii")
    normal = ("1","2","3","4","5","6","7","8")

    def __init__(self,inp):
        self.inp = inp
        conv = input("1 if you want to convert to roman. 2 to convert to normal:")
        if conv == "1":
            self.to_roman()
        elif conv == "2":
            self.to_normal()
    def to_roman(self):
        for i in range(len(self.normal)):
            if self.inp == self.normal[i]:
                print(self.roman[i])
    def to_normal(self):
        for i in range(len(self.roman)):
            if self.inp == self.roman[i]:
                print(self.normal[i])
inp = input("Enter number to convert:")
converter = convert(inp)

#HAD TO USE A TIIIIIINY BUT OF AI BUT UNDERSTOOD MOST OF IT :) DEEPLY.
            
from csv import writer, reader                      # Importing only required functions from csv module

class CSVToTable:                                   # This help to convert CSV to text-based table
    def __init__(self, filename):                   # filename must be csv
        self.file = filename
        self.data = []

    def read(self):
        with open(self.file, "r", newline="") as f:
            r = reader(f)
            self.data = [i for i in r]
            f.close()
    def getWidth(self, column):
        width = 0
        for i in range(len(self.data)):
            if len(self.data[i][column])>width:
                width = len(self.data[i][column])
        return width

    def displayTable(self):                         # Call this method to display table
        def writerow(val):
            row = "| "
            for it in range(len(self.data[0])):
                d = ""
                for j in range(self.getWidth(it)):
                    try:
                        d += val[it][j]
                    except IndexError:
                        for k in range(self.getWidth(it)-j):
                            d += " "
                        break
                row += d
                row += " | "
            return row

        self.read()

        row_sep = "+"
        for col in range(len(self.data[0])):
            row_sep += "-" * (self.getWidth(col)+2)
            row_sep += "+"

        table = f"{row_sep}\n" \
                f"{writerow(self.data[0])}\n" \
                f"{row_sep}\n"
        for i in range(1, len(self.data)):
            table += writerow(self.data[i])
            table += "\n"
        table += row_sep
        return table

if __name__ == "__main__":
    _class = CSVToTable("Student.csv")
    print(_class.displayTable())         # Run Our Code
    input("")

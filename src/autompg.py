from collections import namedtuple
import csv
import os


class AutoMPG:
    """
    A class that represents make, model, year, and mpg attributes
    for each record in the data set.

    Attributes
    ----------
    make (str): make of car
    model(str): model of car
    year(int): year car was made
    mpg(float): miles per gallon of car

    Methods
    -------
    __repr__: Outputs an unambiguous representation of the class object; for developers.
    __str__: Human-readable representation of class object; for end-users. 
    __eq__: Evaluates whether 2 AutoMPG instances are equivalent based on make, model, year, and mpg
    __lt__: Evaluates whether an AutoMPG instance is less than the other based on make, model, year, and mpg
    __hash__: Makes class hashable again after defining __eq__ method
    """

    def __init__(self, make: str, model: str, year: int, mpg: float):
        self.make = make
        self.model = model
        self.year = year
        self.mpg = mpg


    def __repr__(self):
        """
        Outputs an unambiguous representation of the class object; for developers.

        Return:
          (str): A formal string representation of AutoMPG with attribute names and values.
        """
        return f"AutoMPG(make='{self.make}', model='{self.model}', year={self.year}, mpg={self.mpg})"


    def __str__(self):
        """
        Human-readable representation of class object; for end-users. 

        Return:
          (str): A readable string summarizing the key attributes of AutoMPG.
        """
        return f'AutoMPG Object of car: {self.make} {self.model}, year: {self.year}, mpg: {self.mpg}'


    def __eq__(self, other):
        """
        Evaluates whether 2 AutoMPG instances are equivalent
        based on make, model, year, and mpg.

        Args:
          other (AutoMPG): The other AutoMPG instance to compare against.

        Return:
          (bool): True if both instances have the same make, model, year, and mpg; False otherwise.
          
        Raises: 
          NotImplemented: raised for binary special methods (eq, lt, add, rsub) to indicate 
          the operation is not implemented with respect to the other type.

        """
        # self type will always be AutoMPG object, since it is an object of the class
        if type(self) == type(other):
          return (self.make, self.model, self.year, self.mpg) == \
                (other.make, other.model, other.year, other.mpg)
        else:
          raise NotImplemented
        

    def __lt__(self, other):
        """
        Compares two AutoMPG instances to determine if the current instance
        is less than the other instance based on make, model, year, and mpg.
        
        If any qualities are greater than or equivalent, it returns False.

        Args:
          other (AutoMPG): The other AutoMPG instance to compare against.

        Return:
          (bool): True if the current instance is considered 'less than' the 
          other based on make, model, year, and mpg; False otherwise.

        """
        if type(self) == type(other):
          
          if (self.make, self.model, self.year, self.mpg) == \
                    (other.make, other.model, other.year, other.mpg):
            return False
          elif (self.make > other.make or
                self.model > other.model or
                self.year > other.year or
                self.mpg > other.mpg):
            return False
          else:
            return True
          
        else:
          return NotImplemented 
        

    def __hash__(self):
        """
        Takes class attributes and returns the hash of the tuple value in which
        each attribute was stored. Makes class hashable again after defining
        __eq__ method.

        Return:
          (int): hash value
        """
        return hash((self.make, self.model, self.year, self.mpg,))


class AutoMPGData:
    """
    An iterable class that will read in the data file, clean it, and generate 
    a list of AutoMPG objects.

    Attributes
    ----------
    data (list): a list of AutoMPG objects (cars)

    Methods
    -------
    __iter__: makes class iterable
    _load_data: Reads in the cleaned data file, and populates self.data with AutoMPG 
    objects.
    _clean_data: Reads in messy data, standardizes data rows and stores the cleaned 
    data in auto_mpg.clean.txt. 
    """


    def __init__(self):
        self.data = []
        self._load_data()


    def __iter__(self):
        """
        Returns an iterator for the `data` attribute of the AutoMPG instance.

        Args:
          file_path (str): name or filepath of data file. 
        
        Returns: An iterator for the `data` attribute of the instance.
        """
        return iter(self.data)


    def _load_data(self, file_path = 'data/auto-mpg.clean.txt'):
        """
        Reads in the cleaned data file, and populates self.data with AutoMPG objects.

        If the data file does not exist, it triggers the data cleaning process by calling
        the _clean_data() method. The file is expected to have space-separated values 
        representing the car's attributes: mpg, cylinders, displacement, horsepower, weight, 
        acceleration, year, origin, make, and model.
        """
        # Creates data file it it doesn't exist
        if not os.path.exists(file_path):
            self._clean_data()
            
        # Create namedtuple to store records
        Record = namedtuple('Record', ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
                                       'acceleration', 'year', 'origin', 'make', 'model'])
        
        # Reads in data from data file
        try: 
          with open(file_path, 'r') as f:
              reader = csv.reader(f)
              
              for data in reader:
                  line = data[0]
                  split_list = line.split(' ', maxsplit=9)
                  
                  # ensure each line has correct number of attributes
                  if len(split_list) < 10:
                      continue
                  
                  # add 19 in front of year, cast mpg as float
                  year = int("19" + split_list[6])
                  mpg = float(split_list[0])
                  
                  # #repackage lines into a namedtuple
                  # print(Record(split_list[0], split_list[1], split_list[2], split_list[3], split_list[4],
                  # split_list[5], split_list[6], split_list[7], split_list[8], split_list[9]), end="\n\n")
                  car_tuple = Record(mpg, split_list[1], split_list[2], split_list[3], split_list[4],
                                    split_list[5], year, split_list[7], split_list[8], split_list[9])
                  
                  
                  
                  # create an AutoMPG object using the parsed data
                  car = AutoMPG(car_tuple.make, car_tuple.model, car_tuple.year, car_tuple.mpg)
                  self.data.append(car)
        
        except FileNotFoundError:
          print(f"Error: The file {file_path} was not found.")
        except IOError as e:
          print(f"Error: {e}. Likely incorrect filename or location.")


    def _clean_data(self, clean_file = 'data/auto-mpg.clean.txt', messy_file = 'data/auto-mpg.data.txt'):
        """
        Reads in messy data, standardizes data rows and stores the cleaned
        data in auto_mpg.clean.txt. 
        
        Args:
          clean_file (str): file path to file with standardized data
          messy_file (str): file path to file with non-standardized data
        """
        with open(clean_file, "w+") as wf:
            with open(messy_file, "r") as rf:
                contents = csv.reader(rf)
                for line in contents:
                    wf.writelines(" ".join(line[0].split(maxsplit=8)) + "\n")



def main():
    """
    Instantiates an AutoMPGData object. Iterates over the `data` (list) 
    attribute of the instance. 

    Return: None
    """
    auto_list = AutoMPGData()
    
    for car in auto_list:
        print(car)


if __name__ == "__main__":
    main()
    
    car_1 = AutoMPG('bmw', 'x3', 2013, 7.8)
    car_2 = AutoMPG('chevy', 'truck', 2010, 10.8)
    car_3 = AutoMPG('chevy', 'truck', 2010, 10.8)
    car_4 = AutoMPG('audi', 'a4', 2009, 9.8)
    print(f"\n{car_1}")
    print(car_2)

    print("\nTesting equality between car_1 and car_2:", car_1 == car_2)
    print("Should be False:", car_1 == car_3)
    print("Should be True:", car_3 == car_2)

    print("\nTesting lt. Should be True:", car_4 < car_3)
    print("Should be False:", car_3 < car_4)

    # Testing hash method:
    # sets, like dict key, can only take hashable types.
    # sets asks hash method how to deal with duplicate values.
    # Excludes duplicate car object.
    test_hash = {car_1, car_2, car_3, car_4}
    print("\nHash test:", test_hash)
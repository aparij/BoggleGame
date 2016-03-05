import enchant
from itertools import permutations

class Boggle:

    def __init__(self,letters,size):
        self.size = size
        self.grid = self.init_grid(letters,size)
        self.dictionary = enchant.Dict("en_US")

    def get_permutations(self,s):
        all_s_perms = []
        length_of_perms = range(3,len(s)+1)
        for l in length_of_perms:
            all_s_perms.extend([''.join(p) for p in permutations(s,l)])
        return all_s_perms

    def get_all_possible_words(self):
        possible_words = set()
        for s in self.generate_strings():
            all_perms = self.get_permutations(s)
            #print all_perms
            for permutation in all_perms:
                if self.is_valid_word(permutation):
                    possible_words.add((permutation))

        return possible_words

    def init_grid(self, letters_seq, grid_size):
        """

        :param letters_seq: one long string of all the letter left to right, top to bottom rows
        :param grid_size: number , if the board is 4x4 then 4
        :return:

            list of lists grid_size x grid_size
        """

        grid = [['']*grid_size for y in range(grid_size)]
        i = 0
        j = 0
        for letter in letters_seq:
            grid[j][i] = letter
            i += 1
            if i % (grid_size) == 0:
                i = 0
                j += 1

        return grid

    def generate_strings(self):
         '''

         :return:

         '''

         all_strings=[]

         for j in range(self.size): #rows
            for i in range(self.size): #columns
                s = ''
                s += self.grid[j][i]

                # \ | /
                # - X -
                # / | \
                #to the right of current letter
                if i<self.size-1:
                    s += self.grid[j][i+1]
                #to the left of current letter
                if i!=0:
                    s += self.grid[j][i-1]
                #below the current letter
                if j<self.size-1:
                    s += self.grid[j+1][i]
                #above the current letter
                if j!=0:
                    s += self.grid[j-1][i]

                #DIAGONALS
                #diagonal left upper
                if j!=0 and i!=0:
                    s += self.grid[j-1][i-1]
                #diagonal right upper
                if j!=0 and i<self.size-1:
                    s += self.grid[j-1][i+1]
                #diagonal left lower
                if j<self.size-1 and i!=0:
                    s += self.grid[j+1][i-1]
                #diagonal right lower
                if j<self.size-1 and i<self.size-1:
                    s += self.grid[j+1][i+1]

                all_strings.append(s)

         return all_strings


    def is_valid_word(self,s):
        return self.dictionary.check(s)


    def __repr__(self):
        r = ''
        for row in self.grid:
            r += str(row) + '\n'
        return r
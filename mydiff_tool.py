from __future__ import print_function  # Py2 compat
from collections import namedtuple
import sys

from config import DEFAULT_PATH, ORIGINAL, NEW


# ! Хочу решить тут задачу на реализацию diff app
# TODO:
# * алгоритмы, сложность
# * какие алгоритмы используются для реализации diff
Keep = namedtuple('Keep', ['line', 'index'])
Insert = namedtuple('Insert', ['line', 'index'])
Remove = namedtuple('Remove', ['line', 'index'])

# See frontier in myers_diff
Frontier = namedtuple('Frontier', ['x', 'history'])


def myers_diff(a_lines, b_lines):
    """
    An implementation of the Myers diff algorithm.
    See http://www.xmailserver.org/diff2.pdf
    """
    # This marks the farthest-right point along each diagonal in the edit
    # graph, along with the history that got it there
    frontier = {1: Frontier(0, [])}


    def one(idx):
        """
        The algorithm Myers presents is 1-indexed; since Python isn't, we
        need a conversion.
        """
        return idx - 1

    a_max = len(a_lines)
    b_max = len(b_lines)
    index_b = []
    index_a = []
    for d in range(0, a_max + b_max + 1):
        for k in range(-d, d + 1, 2):
            # This determines whether our next search point will be going down
            # in the edit graph, or to the right.
            #
            # The intuition for this is that we should go down if we're on the
            # left edge (k == -d) to make sure that the left edge is fully
            # explored.
            #
            # If we aren't on the top (k != d), then only go down if going down
            # would take us to territory that hasn't sufficiently been explored
            # yet.
            go_down = (k == -d or (k != d and frontier[k - 1].x < frontier[k + 1].x))

            # Figure out the starting point of this iteration. The diagonal
            # offsets come from the geometry of the edit grid - if you're going
            # down, your diagonal is lower, and if you're going right, your
            # diagonal is higher.
            if go_down:
                old_x, history = frontier[k + 1]
                x = old_x
            else:
                old_x, history = frontier[k - 1]
                x = old_x + 1
            history = history[:]
            y = x - k
            index_start_a, index_end_a = 0, 0
            index_start_b, index_end_b = 0, 0
            print ('s')
            if 1 <= y <= b_max and go_down:
                history.append(Insert(line=b_lines[one(y)], index=one(y)))
                print('b', Insert(line=b_lines[one(y)], index=one(y)))
            elif 1 <= x <= a_max:
                history.append(Remove(a_lines[one(x)], index=one(x)))
                print('a', Remove(a_lines[one(x)], index=one(x)))
            while x < a_max and y < b_max and a_lines[one(x + 1)] == b_lines[one(y + 1)]:
                x += 1
                y += 1
                history.append(Keep(a_lines[one(x)], index=one(x)))
                print('a', Keep(a_lines[one(x)], index=one(x)))
            input('e')
            if x >= a_max and y >= b_max:
                return history
            else:
                frontier[k] = Frontier(x, history)

    assert False, 'Could not find edit script'


def main():
    # try:
    #     _, a_file, b_file = sys.argv
    # except ValueError:
    #     print(sys.argv[0], '<FILE>', '<FILE>')
    #     return 1
    a_file = DEFAULT_PATH + '\\' + ORIGINAL
    b_file = DEFAULT_PATH + '\\' + NEW
    with open(file=a_file, mode='r', encoding='utf-8') as a_handle:
        a_lines = [line.rstrip() for line in a_handle]
    with open(file=b_file, mode='r', encoding='utf-8') as b_handle:
        b_lines = [line.rstrip() for line in b_handle]
    # diff = myers_diff(a_lines, b_lines)
    # # print(diff)
    # for elem in diff:
    #     if isinstance(elem, Keep):
    #         print(' ' + elem.line)
    #     elif isinstance(elem, Insert):
    #         print('+' + elem.line)
    #     else:
    #         print('-' + elem.line)


if __name__ == '__main__':
    sys.exit(main())
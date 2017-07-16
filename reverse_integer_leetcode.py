class Solution(object):
    def reverse(self, x):

        string = str(x)
        temp = list(string)
        # print temp
        if temp[0] == '-':
            l = []
            for i in range(1, len(temp)):
                l.append(temp[i])
            l = l[::-1]
            # print l
            string_final = "".join(l)
            string_final = '-' + string_final
            num = int(string_final)
            if num < -2147483648:
                return 0
            else:
                return num
        else:
            l = []
            for i in range(0, len(temp)):
                l.append(temp[i])
            l = l[::-1]
            string_final = "".join(l)
            num = int(string_final)
            if num > 2147483648:
                return 0
            else:
                return num

        """
        :type x: int
        :rtype: int
        """

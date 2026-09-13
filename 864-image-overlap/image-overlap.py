class Solution(object):
    def largestOverlap(self, img1, img2):

        n = len(img1)

        points1 = []
        points2 = []

        # Store coordinates of all 1s
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    points1.append((i, j))

                if img2[i][j] == 1:
                    points2.append((i, j))

        count = {}

        # Compare every 1 in img1 with every 1 in img2
        for x1, y1 in points1:
            for x2, y2 in points2:

                dx = x2 - x1
                dy = y2 - y1

                if (dx, dy) not in count:
                    count[(dx, dy)] = 0

                count[(dx, dy)] += 1

        # Maximum number of pairs having same translation
        if count:
            return max(count.values())

        return 0
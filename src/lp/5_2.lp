/* Objective function */
min: +C7 +C8;

/* Constraints */
+170 C1 +114 C2 -200 C5 <= 0;
+170 C3 +114 C4 -200 C6 <= 0;
+2 C1 +2 C2 -7 C5 <= 0;
+2 C3 +2 C4 -7 C6 <= 0;
+C1 +C3 = 1;
+C2 +C4 = 1;
+2 C1 +2 C2 -2 C3 -2 C4 -C7 <= 0;
-2 C1 -2 C2 +2 C3 +2 C4 -C7 <= 0;
-2 C1 -2 C2 +2 C3 +2 C4 -C8 <= 0;
+2 C1 +2 C2 -2 C3 -2 C4 -C8 <= 0;

/* Variable bounds */
C1 <= 1;
C2 <= 1;
C3 <= 1;
C4 <= 1;
C5 <= 1;
C6 <= 1;

/* Integer definitions */
int C1,C2,C3,C4,C5,C6,C7,C8;

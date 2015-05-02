/* Objective function */
min: +C5;

/* Constraints */
+170 C1 +114 C2 +170 C3 +114 C4 -200 C5 <= 0;
+2 C1 +2 C2 +2 C3 +2 C4 -7 C5 <= 0;
+C1 +C3 = 1;
+C2 +C4 = 1;

/* Variable bounds */
C1 <= 1;
C2 <= 1;
C3 <= 1;

/* Integer definitions */
int C1,C2,C3,C5;

/* Objective function */
min: +C5;

/* Constraints */
+170 C1 +114 C2 <= 200;
+170 C3 +114 C4 <= 200;
+2 C1 +2 C2 <= 7;
+2 C3 +2 C4 <= 7;
+C1 +C3 = 1;
+C2 +C4 = 1;
+2 C1 +2 C2 -2 C3 -2 C4 -C5 <= 0;
-2 C1 -2 C2 +2 C3 +2 C4 -C5 <= 0;

/* Variable bounds */
C1 <= 1;
C2 <= 1;
C3 <= 1;
C4 <= 1;

/* Integer definitions */
int C1,C2,C3,C4,C5;

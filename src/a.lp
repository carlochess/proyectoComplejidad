/* Objective function */
min: +C11 +C12;

/* Constraints */
+3 C1 +7 C2 +20 C3 +4 C4 -30 C9 <= 0;
+3 C5 +7 C6 +20 C7 +4 C8 -30 C10 <= 0;
+19 C1 +8 C2 +5 C3 +C4 -20 C9 <= 0;
+19 C5 +8 C6 +5 C7 +C8 -20 C10 <= 0;
+C1 +C5 = 1;
+C2 +C6 = 1;
+C3 +C7 = 1;
+C4 +C8 = 1;
+19 C1 +8 C2 +5 C3 +C4 -19 C5 -8 C6 -5 C7 -C8 -C11 = 1;
-19 C1 -8 C2 -5 C3 -C4 +19 C5 +8 C6 +5 C7 +C8 -C11 = 1;
-19 C1 -8 C2 -5 C3 -C4 +19 C5 +8 C6 +5 C7 +C8 -C12 = 1;
+19 C1 +8 C2 +5 C3 +C4 -19 C5 -8 C6 -5 C7 -C8 -C12 = 1;

/* Variable bounds */
C1 <= 1;
C2 <= 1;
C3 <= 1;
C4 <= 1;
C5 <= 1;
C6 <= 1;
C7 <= 1;
C8 <= 1;
C9 <= 1;
C10 <= 1;

/* Integer definitions */
int C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12;

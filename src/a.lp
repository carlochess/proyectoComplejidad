/* Objective function */
min: +C11 +C12;

/* Constraints */
+20 C1 +20 C2 +20 C3 +20 C4 +20 C5 -40 C11 <= 0;
+20 C6 +20 C7 +20 C8 +20 C9 +20 C10 -40 C12 <= 0;
+20 C1 +20 C2 +20 C3 +20 C4 +20 C5 -40 C11 <= 0;
+20 C6 +20 C7 +20 C8 +20 C9 +20 C10 -40 C12 <= 0;
+C1 +C5 = 1;
+C2 +C6 = 1;
+C3 +C7 = 1;
+C4 +C8 = 1;
+C5 +C9 = 1;

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
C11 <= 1;
C12 <= 1;

/* Integer definitions */
int C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12;

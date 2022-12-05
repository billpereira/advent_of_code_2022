      *****************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. ADV1.
       AUTHOR. billpereira.
      *****************************************************************
       ENVIRONMENT DIVISION. 
       INPUT-OUTPUT SECTION.
       FILE-CONTROL. 
           SELECT CALORY_FILE ASSIGN TO INPUTDD
           ORGANIZATION IS SEQUENTIAL
           ACCESS MODE IS SEQUENTIAL.

      *****************************************************************
       DATA DIVISION. 

       FILE SECTION.
       FD  CALORY_FILE 
           RECORDING MODE IS F
           DATA RECORD IS CALORY_LINE.
       01 CALORY_LINE.
          05 CALORY_VALUE     PIC X(5) JUSTIFIED RIGHT.
          05 FILLER           PIC X(75).

       WORKING-STORAGE SECTION. 
       01 ELF_INDEX           PIC 9(10) VALUE ZEROS.      
       01 CURRENT_SUM         PIC 9(10) VALUE ZEROS.      
       01 CALORY              PIC 9(10) VALUE ZEROS.      
       01 BIGGEST_ELF         PIC 9(10) VALUE ZEROS.      
       01 BIGGEST_SUM         PIC 9(10) VALUE ZEROS.      
       01 SECOND_BIGGEST_ELF  PIC 9(10) VALUE ZEROS.      
       01 SECOND_BIGGEST_SUM  PIC 9(10) VALUE ZEROS.      
       01 THIRD_BIGGEST_ELF   PIC 9(10) VALUE ZEROS.      
       01 THIRD_BIGGEST_SUM   PIC 9(10) VALUE ZEROS.     
       01 TOTAL_SUM           PIC 9(10) VALUE ZEROS.     
       01 WS-EOF              PIC A(1). 
      *****************************************************************
       PROCEDURE DIVISION.

       CALCULATE-CALORIES.
           OPEN INPUT CALORY_FILE.
           PERFORM UNTIL WS-EOF = 'Y'
                   READ CALORY_FILE NEXT RECORD
                   AT END
                      MOVE 'Y' TO WS-EOF
                   NOT AT END
                       IF CALORY_VALUE = SPACES THEN
                          PERFORM CHECK_CALORIES 
                          ADD 1 TO ELF_INDEX
                          MOVE ZEROES TO CURRENT_SUM 
                       ELSE 
                          UNSTRING CALORY_VALUE DELIMITED ALL SPACE
                             INTO CALORY
                          ADD CALORY TO CURRENT_SUM
                       END-IF 
                   END-READ
           END-PERFORM.
           CLOSE CALORY_FILE.

           ADD BIGGEST_SUM TO TOTAL_SUM 
           ADD SECOND_BIGGEST_SUM TO TOTAL_SUM 
           ADD THIRD_BIGGEST_SUM TO TOTAL_SUM 

           DISPLAY "Hello World!".
           DISPLAY "1ST ELF: "
                   BIGGEST_ELF
                   "SUM: "
                   BIGGEST_SUM.
           DISPLAY "2ND ELF: "
                   SECOND_BIGGEST_ELF
                   "SUM: "
                   SECOND_BIGGEST_SUM.
           DISPLAY "3RD ELF: "
                   THIRD_BIGGEST_ELF
                   "SUM: "
                   THIRD_BIGGEST_SUM.
           DISPLAY "TOTAL 3 BIGGEST: "
                   THIRD_BIGGEST_SUM.
           STOP RUN. 

       CHECK_CALORIES.
           IF CURRENT_SUM >= BIGGEST_SUM THEN
              MOVE SECOND_BIGGEST_SUM TO THIRD_BIGGEST_SUM
              MOVE SECOND_BIGGEST_ELF TO THIRD_BIGGEST_ELF
              MOVE BIGGEST_ELF TO SECOND_BIGGEST_ELF
              MOVE BIGGEST_SUM TO SECOND_BIGGEST_SUM
              MOVE CURRENT_SUM TO BIGGEST_SUM
              MOVE ELF_INDEX TO BIGGEST_ELF
           ELSE 
              IF CURRENT_SUM >= SECOND_BIGGEST_SUM THEN 
                 MOVE SECOND_BIGGEST_SUM TO THIRD_BIGGEST_SUM
                 MOVE SECOND_BIGGEST_ELF TO THIRD_BIGGEST_ELF
                 MOVE CURRENT_SUM TO SECOND_BIGGEST_SUM
                 MOVE ELF_INDEX TO SECOND_BIGGEST_ELF
              ELSE
                 IF CURRENT_SUM >= THIRD_BIGGEST_SUM THEN 
                    MOVE CURRENT_SUM TO THIRD_BIGGEST_SUM
                    MOVE ELF_INDEX TO THIRD_BIGGEST_ELF
                 END-IF 
              END-IF 
           END-IF. 

       END PROGRAM ADV1.
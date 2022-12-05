      *****************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. ADV2.
       AUTHOR. billpereira.
      *****************************************************************
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT MATCHES ASSIGN TO INPUTDD
           ORGANIZATION IS SEQUENTIAL
           ACCESS MODE IS SEQUENTIAL.

      *****************************************************************
       DATA DIVISION.

       FILE SECTION.
       FD  MATCHES
           RECORDING MODE IS F
           DATA RECORD IS MATCH_LINE.
       01 MATCH_LINE.
          05 OPPONENT_HAND   PIC X(1).
          05 FILLER          PIC X(1).
          05 DESIRED_RESULT  PIC X(1).
          05 FILLER          PIC X(77).

       WORKING-STORAGE SECTION.
       01 CURRENT_SUM        PIC 9(10).
       01 CURRENT_SCORE      PIC 9(1).
       01 RESULT             PIC X(5).
       01 WS-EOF             PIC A(1).
      *****************************************************************
       PROCEDURE DIVISION.

       ROCK-PAPER-SCISSORS.
           OPEN INPUT MATCHES.
           PERFORM UNTIL WS-EOF = 'Y'
                   READ MATCHES NEXT RECORD
                   AT END
                      MOVE 'Y' TO WS-EOF
                   NOT AT END
                       PERFORM DEFINE_RESULT
                       PERFORM CHOOSE_HAND 
                       ADD CURRENT_SCORE TO CURRENT_SUM
                       DISPLAY "Opponent Hand: "
                               OPPONENT_HAND
                               " RESULTS: "
                               RESULT
                               " ADDING "
                               CURRENT_SCORE
                               " POINTS - CURRENT SUM OF SCORES: "
                               CURRENT_SUM
                       MOVE ZEROES TO CURRENT_SCORE

                   END-READ
           END-PERFORM.
           CLOSE MATCHES.

           DISPLAY "POINTS: " CURRENT_SUM 

           STOP RUN.

       DEFINE_RESULT.
           IF DESIRED_RESULT = 'X' THEN
              MOVE 'LOOSE' TO RESULT
           END-IF.
           IF DESIRED_RESULT = 'Y' THEN
              MOVE 'DRAWN' TO RESULT
           END-IF.
           IF DESIRED_RESULT = 'Z' THEN
              MOVE 'WIN' TO RESULT
           END-IF.
       
       CHOOSE_HAND.
           EVALUATE OPPONENT_HAND ALSO RESULT
      *    ADD 1 FOR ROCK HAND - A 
      * .  ADD 2 FOR PAPER HAND - B 
      * .  ADD 3 FOR SCISSORS - C
      *    ADD 0 FOR LOOSE
      *    ADD 3 FOR DRAWN
      *    ADD 6 FOR WIN
           WHEN 'A' ALSO 'LOOSE'
                DISPLAY "ADDING 3 FOR LOOSING WITH SCISSOR"
                ADD 3 TO CURRENT_SCORE
           WHEN 'A' ALSO 'DRAWN'
                DISPLAY "ADDING 4 FOR DRAWN WITH ROCK"
                ADD 1 TO CURRENT_SCORE
                ADD 3 TO CURRENT_SCORE
           WHEN 'A' ALSO 'WIN  '
                DISPLAY "ADDING 8 FOR WINNING WITH PAPER"
                ADD 2 TO CURRENT_SCORE
                ADD 6 TO CURRENT_SCORE
           WHEN 'B' ALSO 'LOOSE'
                DISPLAY "ADDING 1 FOR LOOSING WITH ROCK"
                ADD 1 TO CURRENT_SCORE
           WHEN 'B' ALSO 'DRAWN'
                DISPLAY "ADDING 5 FOR DRAWN WITH PAPER"
                ADD 2 TO CURRENT_SCORE
                ADD 3 TO CURRENT_SCORE
           WHEN 'B' ALSO 'WIN '
                DISPLAY "ADDING 9 FOR WINNING WITH SCISSOR"
                ADD 3 TO CURRENT_SCORE
                ADD 6 TO CURRENT_SCORE
           WHEN 'C' ALSO 'LOOSE'
                DISPLAY "ADDING 2 FOR LOOSING WITH PAPER"
                ADD 2 TO CURRENT_SCORE
           WHEN 'C' ALSO 'DRAWN'
                DISPLAY "ADDING 6 FOR DRAWN WITH SCISSOR"
                ADD 3 TO CURRENT_SCORE
                ADD 3 TO CURRENT_SCORE
           WHEN 'C' ALSO 'WIN  '
                DISPLAY "ADDING 7 FOR WINNING WITH ROCK"
                ADD 1 TO CURRENT_SCORE
                ADD 6 TO CURRENT_SCORE
           END-EVALUATE.
                  

       END PROGRAM ADV2.
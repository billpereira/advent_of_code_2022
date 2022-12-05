/* REXX */
INPUT_DSN='Z93415.ADVCODE.INPUT(DAY2)'

current_sum = 0
own_shapes_value.Y = 2
own_shapes_value.X = 1
own_shapes_value.Z = 3
loose_table.A = "Z"
loose_table.B = "X"
loose_table.C = "Y" 
drawn_table.A = "X"
drawn_table.B = "Y"
drawn_table.C = "Z"
win_table.A = "Y"
win_table.B = "Z"
win_table.C = "X"
current_score = 0
/* 
teste = 'x'
 
say value(own_shapes_value.||teste) */

ADDRESS TSO
"ALLOC F(INPUTDD) DA('"||INPUT_DSN||"') SHR"
"EXECIO * DISKR INPUTDD (FINIS STEM MATCHES."
DO i = 1 to MATCHES.0
 if substr(MATCHES.i,3,1) == "X" then 
 do 
  result_value = 0
  index_loose_table = substr(MATCHES.i,1,1)
  index_own_shapes_value = value(loose_table.||index_loose_table)
  shape_value =  value(own_shapes_value.||index_own_shapes_value)
  current_score= result_value + shape_value
 end
 if substr(MATCHES.i,3,1) == "Y" then 
 do 
  result_value = 3
  index_drawn_table = substr(MATCHES.i,1,1)
  index_own_shapes_value = value(drawn_table.||index_drawn_table)
  shape_value =  value(own_shapes_value.||index_own_shapes_value)
  current_score= result_value + shape_value
 end
 if substr(MATCHES.i,3,1) == "Z" then 
 do 
  result_value = 6
  index_win_table = substr(MATCHES.i,1,1)
  index_own_shapes_value = value(win_table.||index_win_table)
  shape_value =  value(own_shapes_value.||index_own_shapes_value)
  current_score= result_value + shape_value
 end
 /* say "current_score ="current_score */
 current_sum = value(current_sum) + value(current_score)
END
"FREE F(INPUTDD)"
say current_sum
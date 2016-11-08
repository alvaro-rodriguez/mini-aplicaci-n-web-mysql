% include('aplication.tpl')
Query out
<p>+--------------------------------------------------------------------+</p>
%for row in cursor.fetchall():
   <p>|</p>
  %for r in row:
   | {{r}}  
  %end
%end

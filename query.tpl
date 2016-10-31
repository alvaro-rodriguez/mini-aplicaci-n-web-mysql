% include('aplication.tpl')
<p>+--------------------------------------------------------------------+</p>
%for row in cursor.fetchall():
  <p>+------------------------+</p>
  %for r in row:
    <p>{{r}}</p>
  %end
%end
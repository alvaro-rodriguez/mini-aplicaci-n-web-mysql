% include('header.tpl')
<p>QUERY</p>
   <body>
    <p>QUERY:</p>
    <br />
    <form action="/query" method="post">
    <p>Usuario:<textarea name="user" id="textbox" rows="1" cols="10"></textarea>
    Contraseña:<textarea name="password" id="textbox" rows="1" cols="10"></textarea>
      Host:<textarea name="host" id="textbox" rows="1" cols="10"></textarea>
      Base de datos:<textarea name="database" id="textbox" rows="1" cols="10"></textarea>
      <p><textarea name="query" id="textbox" rows="3" cols="100"></textarea></p>
      <p><input type="submit" class="button" value="Enviar" /></p>
    </form>
    
    <a href="/menu">Cancelar</a>
  
  </body>

            

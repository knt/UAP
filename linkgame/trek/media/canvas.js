  <script type="text/javascript">

  var lastx = (500 / 2);
  var lasty = 2.5;
  var drawArrow = false;
  
  function draw(str){
  var canvas = document.getElementById("canvas");
  var paddingW = 20;
  var paddingH = 20;
  var cvWidth = $("#canvas").width();

  if (canvas.getContext){  
  var ctx = canvas.getContext("2d");
  ctx.textAlign = "center";
  ctx.lineWidth = 1.0;
  ctx.textBaseline = "middle";
  ctx.font = "1em sans-serif";
  ctx.lineJoin = "round";
  //ctx.fillText('{{ concept1 }}', 60, 60);
  // ctx.beginPath();  
  // ctx.arc(75,75,50,0,Math.PI*2,true); // Outer circle  
  // ctx.stroke();   


  var metrics = ctx.measureText(str);
  var nodeWidth = metrics.width + paddingW;
  var nodeHeight = 30;

  if (drawArrow == true) {

  var arrowLength = lasty + 30;

  ctx.beginPath();
  ctx.moveTo(lastx, lasty);
  ctx.lineTo(lastx, arrowLength);
  ctx.lineTo(lastx + 5, arrowLength - 5);
  ctx.moveTo(lastx - 5, arrowLength - 5);
  ctx.lineTo(lastx, arrowLength);
  ctx.stroke();
  ctx.closePath();

  lasty = arrowLength + 6;

}

  draw_node(ctx, lastx-(nodeWidth/2), lasty, nodeWidth, nodeHeight);
  ctx.fillText(str, lastx+(nodeWidth/2)-(nodeWidth/2), lasty+(nodeHeight/2));
  lastx = lastx;
  lasty = lasty + nodeHeight;

drawArrow = true;
  } else {  
  // canvas-unsupported code here  
  }  }


  function draw_node(context, x, y, width, height) {
  context.strokeRect(x, y, width,  height );
  };
  </script>
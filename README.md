
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Aaaagni | Pink Home</title>
<style>
*{
  margin:0;
  padding:0;
  box-sizing:border-box;
}
body{
  min-height:100vh;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  background:
    radial-gradient(circle at 10% 10%, rgba(255,182,193,0.8), transparent 50%),
    radial-gradient(circle at 90% 20%, rgba(255,228,235,0.9), transparent 50%),
    linear-gradient(135deg,#fff0f6,#ffe4ec,#ffd6e0);
  display:flex;
  align-items:center;
  justify-content:center;
  padding:20px;
}
.card{
  width:100%;
  max-width:520px;
  background:rgba(255,255,255,0.78);
  backdrop-filter:blur(20px);
  -webkit-backdrop-filter:blur(20px);
  border-radius:24px;
  padding:48px 36px;
  box-shadow:
    0 10px 40px rgba(255,105,180,0.25),
    0 0 0 1px rgba(255,255,255,0.8);
  text-align:center;
}
.avatar{
  width:120px;
  height:120px;
  border-radius:50%;
  background:linear-gradient(135deg,#ff9bb4,#ff66a3);
  display:flex;
  align-items:center;
  justify-content:center;
  margin:0 auto 24px;
  font-size:48px;
  box-shadow:0 8px 20px rgba(255,105,180,0.35);
}
h1{
  font-size:36px;
  color:#d63384;
  margin-bottom:8px;
}
.sub{
  color:#ff8fab;
  font-size:18px;
  margin-bottom:24px;
}
.line{
  width:60px;
  height:4px;
  background:linear-gradient(90deg,#ff9bb4,#ff66a3);
  border-radius:2px;
  margin:0 auto 28px;
}
p{
  color:#6b7280;
  font-size:16px;
  line-height:1.8;
  margin-bottom:14px;
}
.links{
  margin-top:32px;
  display:flex;
  gap:12px;
  flex-wrap:wrap;
  justify-content:center;
}
.links a{
  text-decoration:none;
  background:linear-gradient(135deg,#ff9bb4,#ff66a3);
  color:white;
  padding:12px 24px;
  border-radius:999px;
  font-weight:500;
  transition:0.3s;
  box-shadow:0 4px 12px rgba(255,105,180,0.3);
}
.links a:hover{
  transform:translateY(-3px);
  box-shadow:0 8px 20px rgba(255,105,180,0.45);
}
.deco{
  position:absolute;
  width:20px;
  height:20px;
  background:rgba(255,255,255,0.6);
  border-radius:50%;
  animation:float 6s infinite ease-in-out;
}
@keyframes float{
  0%,100%{transform:translateY(0);}
  50%{transform:translateY(-15px);}
}
@media(max-width:480px){
  .card{
    padding:36px 24px;
  }
  h1{
    font-size:28px;
  }
}
</style>
</head>
<body>
  <div class="deco" style="top:10%;left:15%;animation-delay:0s;"></div>
  <div class="deco" style="top:20%;right:20%;animation-delay:1s;"></div>
  <div class="deco" style="bottom:15%;left:25%;animation-delay:2s;"></div>

  <div class="card">
    <div class="avatar">🌸</div>
    <h1>Aaaagni</h1>
    <div class="sub">Welcome to my pink world</div>
    <div class="line"></div>
    <p>这里是我的个人小站，记录学习、项目和生活碎片。</p >
    <p>希望每天都有一点进步，也希望你会喜欢这里✨</p >

    <div class="links">
      <a href=" " target="_blank">GitHub</a >
      <a href="#">项目展示</a >
      <a href="#">关于我</a >
    </div>
  </div>
</body>
</html>

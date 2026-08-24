<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>我的个人主页</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: system-ui, -apple-system, sans-serif;
            background: linear-gradient(135deg, #e0efff, #f3e8ff);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .card {
            background: #ffffff;
            max-width: 520px;
            width: 100%;
            padding: 48px 36px;
            border-radius: 20px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.12);
            text-align: center;
        }
        h1 {
            color: #2c3e50;
            font-size: 32px;
            margin-bottom: 14px;
        }
        .sub-title {
            color: #64748b;
            font-size: 17px;
            margin-bottom: 32px;
        }
        .line {
            width: 80px;
            height: 3px;
            background: #8b5cf6;
            margin: 0 auto 30px;
            border-radius: 2px;
        }
        p {
            color: #475569;
            font-size: 16px;
            line-height: 1.7;
            margin-bottom:16px;
        }
        .links a{
            display: inline‑block;
            text-decoration: none;
            background-color:#8b5cf6;
            color:white;
            padding:12px 26px;
            border-radius:999px;
            margin:8px;
            transition:0.25s;
        }
        .links a:hover{
            background-color:#7c3aed;
            transform: translateY(-2px);
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>👋 你好，我是Aaaagni</h1>
        <div class="line"></div>
        <p class="sub-title">欢迎来到我的 GitHub 个人网站</p >
        <p>这里用来记录学习、项目与随笔。</p >
        <p>持续学习，不断进步✨</p >
        <div class="links">
            <a href=" " target="_blank">我的GitHub</a >
        </div>
    </div>
</body>
</html>

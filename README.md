# 开发


使用django实现一个短链接程序。使用mysql数据库存储，一个短链接映射一组url,每次打开短链接可以随机打开这组url中其中一个
新建一个短链接,可自定义，可随机生成

可以一次性添加一组原始链接


## 表关系模型
- Link 表：保存短链接和原始链接组的映射关系；
    - id（主键）：短链接 id；
    - short：短链接字符串；
    - created_at：创建时间；
    - updated_at：更新时间；
    - user_id（外键，参考 auth.User 表的 id 字段）：创建该链接的用户。
- Url 表：保存原始链接和对应的说明；
    - id（主键）：原始链接 id；
    - url：原始链接字符串；
    - description：原始链接说明；
    - created_at：创建时间；
    - updated_at：更新时间；
    - link_id（外键，参考 Link 表的 id 字段）：对应的 Link 记录的 id。
    - 唯一性约束： (link_id, url)

每一个 Url 对象对应一个短链接 Link 对象，而每个 Link 对象则可以关联多个 Url 对象


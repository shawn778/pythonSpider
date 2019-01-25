import pymysql

'''
artist_infos(artist_id varchar(20),artist_name varchar(40),artist_extend_id varchar(20))
album_infos(album_id varchar(20),album_title varchar(100),album_time varchar(20))
music_infos(music_id varchar(20),music_name varchar(50))
comment_infos(comment_id varchar(20),user_id varchar(20),user_nickname varchar(50),liked_count varchar(20),content text,is_hot BOOL )

'''

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='xroot',
    db='python_spider',
    charset='utf8'
)

cursor = conn.cursor()

'''
根据table_name查询数据
'''


def query_record(table_name):
    sql = 'select * from ' + table_name
    record=cursor.execute(sql)
    return record,cursor.fetchall()


'''
table_name 表名称
 data s数据
 insert_type 插入类型 one|many
'''


def insert_record(table_name, data, insert_type):
    if table_name == 'artist_infos' or table_name == 'album_infos':
        sql = 'insert into ' + table_name + ' values(%s,%s,%s)'
    elif table_name == 'music_infos':
        sql = 'insert into ' + table_name + ' values(%s,%s)'
    elif table_name == 'comment_infos':
        sql = 'insert into ' + table_name + ' values(%s,%s,%s,%s,%s,%s)'
    else:
        return False
    if insert_type == 'one':
        cursor.execute(sql, data)
    elif insert_type == 'many':
        cursor.executemany(sql, data)
    else:
        return False
    conn.commit()

    return True


'''
根据条件创建表
'''


def create_tables(create_type='all'):
    # select table_name from information_schema.tables  where table_schema='pyton_spider'
    artist_infos_sql = '''
      CREATE TABLE artist_infos (
        artist_id varchar(20), 
        artist_name varchar(40),
        artist_extend_id varchar(20)
        )ENGINE=innodb DEFAULT CHARSET=utf8; 
        '''
    album_infos_sql = '''
      CREATE TABLE album_infos (
        album_id varchar(20), 
        album_title varchar(100),
        album_time varchar(20)
        )ENGINE=innodb DEFAULT CHARSET=utf8; 
        '''
    music_infos_sql = '''
     CREATE TABLE music_infos (
        music_id varchar(20), 
        music_name varchar(50)
        )ENGINE=innodb DEFAULT CHARSET=utf8; 
    '''
    comment_infos_sql = '''
      CREATE TABLE comment_infos (
        comment_id varchar(30), 
        user_id varchar(30),
        user_nickname varchar(100),
        liked_count varchar(50),
        content varchar(1000),
        is_hot varchar(10)
        )ENGINE=innodb DEFAULT CHARSET=utf8; 
    '''
    if create_type == 'artists':
        cursor.execute(artist_infos_sql)
    elif create_type == 'albums':
        cursor.execute(album_infos_sql)
    elif create_type == 'musics':
        cursor.execute(music_infos_sql)
    elif create_type == 'comments':
        cursor.execute(comment_infos_sql)
    else:
        cursor.execute(artist_infos_sql)
        cursor.execute(album_infos_sql)
        cursor.execute(music_infos_sql)
        cursor.execute(comment_infos_sql)


def drop_tables(table_name):
    sql = 'drop table ' + table_name
    cursor.execute(sql)


def close():
    cursor.close()
    conn.close()
Artist = ['Calligrapher', 'Designer', 'Architect', 'Sculptor', 'Painter']
Musician = ['Singer', 'Composer', 'Performer', 'Broker']
Dramatist = []
Writer = ['Poet', 'Proser', 'Screenwriter', 'Novelist']

curType = 'Novelist'

def get_Info_list():
    # ArtistList
    if curType == 'Calligrapher':
        return ['http://baike.baidu.com/fenlei/%E4%B9%A6%E6%B3%95%E5%AE%B6?', 11, 'Calligrapher']
    elif curType == 'Designer':
        return ['http://baike.baidu.com/fenlei/%E8%AE%BE%E8%AE%A1%E5%B8%88?', 3, 'Designer']
    elif curType == 'Architect':
        return ['http://baike.baidu.com/fenlei/%E5%BB%BA%E7%AD%91%E5%B8%88?', 2, 'Architect']
    elif curType == 'Sculptor':
        return ['http://baike.baidu.com/fenlei/%E9%9B%95%E5%A1%91%E5%AE%B6?', 1, 'Sculptor']
    elif curType == 'Painter':
        return ['http://baike.baidu.com/fenlei/%E7%94%BB%E5%AE%B6?', 17, 'Painter']
    # MusicianList
    elif curType == 'Singer':
        return ['http://baike.baidu.com/fenlei/%E6%AD%8C%E6%89%8B?', 12, 'Singer']
    elif curType == 'Composer':
        return ['http://baike.baidu.com/fenlei/%E4%BD%9C%E6%9B%B2%E5%AE%B6?', 5, 'Composer']
    elif curType == 'Performer':
        return ['http://baike.baidu.com/fenlei/%E6%BC%94%E5%A5%8F%E5%AE%B6?', 2, 'Performer']
    # elif curType == 'Broker':
    #     return ['http://baike.baidu.com/fenlei/%E7%BB%8F%E7%BA%AA%E4%BA%BA?', 1, 'Person']
    # Dramatist
    elif curType == 'Dramatist':
        return ['http://baike.baidu.com/fenlei/%E5%89%A7%E4%BD%9C%E5%AE%B6?', 1, 'Dramatist']
    # Writer
    elif curType == 'Poet':
        return ['http://baike.baidu.com/fenlei/%E8%AF%97%E4%BA%BA?', 12, 'Poet']
    elif curType == 'Proser':
        return ['http://baike.baidu.com/fenlei/%E6%95%A3%E6%96%87%E5%AE%B6?', 2, 'Proser']
    elif curType == 'Screenwriter':
        return ['http://baike.baidu.com/fenlei/%E5%89%A7%E4%BD%9C%E5%AE%B6?', 1, 'Screenwriter']
    elif curType == 'Novelist':
        return ['http://baike.baidu.com/fenlei/%E5%B0%8F%E8%AF%B4%E5%AE%B6?', 3, 'Novelist']

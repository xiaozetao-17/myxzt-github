import json
import boto3
import datetime
from decimal import Decimal

# 初始化 DynamoDB 客户端
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('mapgps')  # 这里改为你场景的DynamoDB 表名

# 北京经纬度 - 使用 Decimal 类型
beijing_lat = Decimal('39.9042')  # 北京纬度
beijing_lon = Decimal('116.4074')  # 北京经度

# 获取北京时间的函数
def get_beijing_time():
    # 获取当前的 UTC 时间
    utc_now = datetime.datetime.utcnow()
    
    # 定义北京时区偏移量（UTC+8）
    beijing_offset = datetime.timedelta(hours=8)
    
    # 计算北京时间
    beijing_time = utc_now + beijing_offset
    
    return beijing_time.strftime('%Y-%m-%d %H:%M:%S')

def lambda_handler(event, context):
    # 获取北京时间
    beijing_time = get_beijing_time()
    
    # 假设ID是某种唯一标识符，这里我们用当前时间戳作为ID
    current_id = str(int(datetime.datetime.utcnow().timestamp()))
    
    # 数据要写入 DynamoDB
    response = table.put_item(
        Item={
            'id': current_id,
            'beijing_time': beijing_time,
            'latitude': beijing_lat,
            'longitude': beijing_lon
        }
    )
    
    # 注意：在返回时，需要将 Decimal 转换为 float 以便 JSON 序列化
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Data inserted successfully!',
            'id': current_id,
            'beijing_time': beijing_time,
            'latitude': float(beijing_lat),
            'longitude': float(beijing_lon)
        })
    }
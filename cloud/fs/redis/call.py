'''通话相关
'''
from .base import BaseRedis


class CallRedis(BaseRedis):
    '''通话相关redis
    '''
    ring = 'ring-{project_id}'
    queue = 'queue-{project_id}'
    answer = 'answer-{project_id}'

    def get_ring(self, project_id):
        '''获取振铃中
        '''
        ring = self.ring.format(project_id=project_id)
        return self.redis.scard(ring)

    def get_queue(self, project_id):
        '''获取振铃中
        '''
        queue = self.queue.format(project_id=project_id)
        return self.redis.scard(queue, project_id)

    def get_answer(self, project_id):
        '''获取振铃中
        '''
        answer = self.answer.format(project_id=project_id)
        return self.redis.scard(answer, project_id)

    def set_ring(self, project_id, phone_id):
        '''设置振铃中
        '''
        ring = self.ring.format(project_id=project_id)
        self.redis.sadd(ring, phone_id)

    def set_answer(self, project_id, phone_id):
        '''设置客户接通
        '''
        answer = self.answer.format(project_id=project_id)
        self.redis.sadd(answer, phone_id)

    def set_queue(self, project_id, phone_id):
        '''设置坐席接通
        '''
        queue = self.queue.format(project_id=project_id)
        self.redis.sadd(queue, phone_id)

    def clear_redis(self, project_id, phone_id):
        '''清除redis
        '''
        ring = self.ring.format(project_id=project_id)
        answer = self.answer.format(project_id=project_id)
        queue = self.queue.format(project_id=project_id)
        self.redis.srem(ring, phone_id)
        self.redis.srem(queue, phone_id)
        self.redis.srem(answer, phone_id)

from aiopvapi.helpers.aiorequest import AioRequest
from aiopvapi.helpers.api_base import ApiResource
from aiopvapi.helpers.constants import ATTR_SCENE_MEMBER, \
    ATTR_SCENE_ID, ATTR_SHADE_ID


class SceneMember(ApiResource):
    api_path = 'api/scenemembers'

    def __init__(self, raw_data: dict, request: AioRequest):
        if ATTR_SCENE_MEMBER in raw_data:
            raw_data = raw_data.get(ATTR_SCENE_MEMBER)
        super().__init__(request, self.api_path, raw_data)

    # @property
    # def roomId(self):
    #     return self._raw_data.get(SCENE_ROOM_ID)

    # @property
    # def sceneId(self):
    #     return self._

    async def delete(self):
        """Deletes a scene from a shade"""
        _val = await self.request.delete(
            self._base_path,
            params={ATTR_SCENE_ID: self._raw_data.get(ATTR_SCENE_ID),
                    ATTR_SHADE_ID: self._raw_data.get(ATTR_SHADE_ID)})
        return _val
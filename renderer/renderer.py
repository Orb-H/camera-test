from renderer.point_renderer import PointRenderer
from renderer.wireframe_renderer import WireframeRenderer


class Renderer():
    '''
    A base class for renderer.
    '''

    POINT = 1
    WIREFRAME = 2

    def __new__(cls, rendererType, canvas, camera, *vargs, **kwargs):
        '''
        Returns a renderer with type.

        PARAMETER
            rendererType: A int value for defining type of renderer.
                - Renderer.POINT or 1: Point Projector
                - Renderer.WIREFRAME or 2: Wireframe Renderer(Line Only)

            canvas: A tkinter canvas instance to draw on.

            camera: A camera instance.

        RAISES
            Exception if rendererType value is invalid.

        OPTIONS
            for rendererType == Renderer.POINT, any options are not available.

            for rendererType == Renderer.WIREFRAME, 'near' and 'far' options are available.
                - near: A distance to near clipping plane.
                - far: A distance to far clipping plane.
        '''
        if rendererType == 1:
            return PointRenderer(canvas, camera)
        elif rendererType == 2:
            return WireframeRenderer(canvas, camera, vargs, kwargs)
        else:
            raise Exception("Not existing renderer type.")

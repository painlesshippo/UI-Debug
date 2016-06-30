# Under MIT License, see LICENSE.txt

from Model.DataIn.DataInObject import FormatPackageError
from Model.DataIn.DrawingDataIn.BaseDataInDraw import BaseDataInDraw

__author__ = 'RoboCupULaval'


class DrawMultiplePointsDataIn(BaseDataInDraw):
    def __init__(self, data_in):
        BaseDataInDraw.__init__(self, data_in)
        self._format_data()

    def _check_obligatory_data(self):
        """ Vérifie les données obligatoires """
        try:
            assert isinstance(self.data, dict),\
                "data: {} n'est pas un dictionnaire.".format(type(self.data))
            keys = self.data.keys()

            assert 'points' in keys, \
                "data['points'] n'existe pas."
            assert isinstance(self.data['points'], list), \
                "data['points']: {} n'a pas le format attendu (list)".format(type(self.data['points']))
            for i, point in enumerate(self.data['points']):
                assert self._point_is_valid(point), \
                    "data['points'][{}]: {} n'est pas un point valide.".format(i, type(self.data['points']))

        except Exception as e:
            raise FormatPackageError('{}: {}'.format(type(self).__name__, e))

    def _check_optional_data(self):
        """ Vérifie les données optionnelles """
        keys = self.data.keys()
        try:
            if 'color' in keys:
                assert self._colorRGB_is_valid(self.data['color']), \
                    "data['color']: {} n'est pas une couleur valide.".format(self.data['color'])
            else:
                self.data['color'] = (0, 0, 0)

            if 'width' in keys:
                assert isinstance(self.data['width'], int), \
                    "data['width']: {} n'est pas du bon type (int)".format(type(self.data['width']))
            else:
                self.data['width'] = 3

            if 'timeout' in keys:
                assert self.data['timeout'] <= 0, \
                    "data['timeout']: {} n'est pas valide.".format(self.data['timeout'])
            else:
                self.data['timeout'] = 0
        except Exception as e:
            raise FormatPackageError('{}: {}'.format(type(self).__name__, e))

    @staticmethod
    def get_type():
        return 3005
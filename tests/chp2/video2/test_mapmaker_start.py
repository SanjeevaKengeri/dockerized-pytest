from scripts.chp2.video2.mapmaker_start import Point


def test_make_one_point():
    P1 = Point("Dakar", 17.4564, 18.6789)
    assert P1.get_lat_long() == ((17.4564, 18.6789))

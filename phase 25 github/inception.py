
import inception_phase_20_0 as ip_0
import inception_phase_20_1 as ip_1
import inception_phase_20_2 as ip_2
import inception_phase_20_beyond as ip_b
import inception_phase_20_blue as ip_3
#import auto_phase_11 as auto
import pygame
import midi_play

#import auto_phase_11 as auto

def inception(mode,num):
    #mode = 0
    sm = 1
    #num = 4
    if mode == 0:
        ip_0.inception_phase_20_0(sm, num)
    elif mode == 1:
        ip_1.inception_phase_20_1(sm, num)
    elif mode == 2:
        ip_2.inception_phase_20_2(sm, num)
    elif mode == 3:
        ip_b.inception_phase_20_beyond(sm, num)
    else:
        ip_3.inception_phase_20_blue(sm, num)

    #print("hh_0\n")
    import auto_phase_11
    reload(auto_phase_11)
    #print("hh_1\n")
    auto_phase_11.midi_gen()

    if mode == 0:
        tone = 'major'
    elif mode == 1:
        tone = 'minor'
    elif mode == 2:
        tone = 'minor'
    elif mode == 3:
        tone = 'beyond'
    else:
        tone = 'blue'
#print("hh_2\n")
    midi_file = 'inception_phase_11_{}_{}.mid'.format(tone,num)
    midi_play.play_music(midi_file)
#del auto_phase_11

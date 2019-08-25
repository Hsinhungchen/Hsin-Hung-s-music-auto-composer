import random as rand
import pandas_test as pt
import smooth
from inception_include import *

def inception_phase_20_beyond(sm, num):

    mode = 1;
    fp = open("auto_phase_11.py", "w")

#start composing MIDI
    fp.write("#Inception phase 11\n");
    fp.write("import midi\n\n\n")
    fp.write("def midi_gen():\n")
    fp.write("    hh_midi = midi.Pattern(tracks=[[midi.TimeSignatureEvent(tick=0, data=[4, 2, 24, 8]),")
    midi_setup = ["    midi.KeySignatureEvent(tick=0, data=[0, 0]),\n",
              "    midi.EndOfTrackEvent(tick=1, data=[])],\n",
              "    [midi.ControlChangeEvent(tick=0, channel=0, data=[91, 58]),\n",
              "    midi.ControlChangeEvent(tick=0, channel=0, data=[10, 69]),\n",
              "    midi.ControlChangeEvent(tick=0, channel=0, data=[0, 0]),\n",
              "    midi.ControlChangeEvent(tick=0, channel=0, data=[32, 0]),\n",
              "    midi.ProgramChangeEvent(tick=0, channel=0, data=[0]),\n\n"]

    fp.writelines(midi_setup)

#automatic composing
    fp.write("#automatic composing\n")
   
    
    tick_0 = 6400
    tick_1 = 6400
    tick_2 = 9600
    
    beat_0 = 100
    beat_1 = 100
    beat_2 = 200
    
    onset_0 = 0.1
    onset_1 = 0.1
    onset_2 = 0.25

    #if mode == 1:
    chord_1 = A2
    chord_2 = D3
    chord_3 = G3
    chord_4 = C3
    chord_5 = D3
    chord_6 = A2
    chord_7 = F3
    chord_8 = E3
    chord_8_c = A2
    chord_1_b = G3
    chord_2_b = A2
    chord_3_b = G3
    chord_4_b = A2
    chord_5_b = F3
    chord_6_b = F3
    chord_7_b = E3
    chord_8_b = E3
        
    chorus_b_1 = D_7_bass
    chorus_b_2 = A_minor_bass
    chorus_b_3 = D_7_bass
    chorus_b_4 = E_7_bass
    
    chorus_a_1 = A_minor_bass
    chorus_a_2 = C_major_bass
    chorus_a_3 = G_major_bass
    chorus_a_4 = A_minor_bass
        
    chorus_c_1 = F_major_bass
    chorus_c_2 = G_major_bass
    chorus_c_3 = C_major_bass
    chorus_c_4 = G_major_bass
    chorus_c_5 = A_minor_bass
    chorus_c_6 = F_major_bass
    chorus_c_7 = G_major_bass
    chorus_c_8 = A_minor_bass
    
        
    scale_1 = A_minor
    scale_2 = C_major
    scale_3 = G_major
    scale_4 = A_minor
    scale_1_b = D_7
    scale_2_b = A_minor
    scale_3_b = D_7
    scale_4_b = E_7
    
    scale_1_c = F_major
    scale_2_c = G_major
    scale_3_c = C_major
    scale_4_c = G_major
    scale_5_c = A_minor
    scale_6_c = F_major
    scale_7_c = G_major
    scale_8_c = A_minor
    
    
    tone = 'beyond'
    tick_mode = tick_1
    beat = beat_1
    onset_mode = onset_1
    


    tick = 0
    note = 72;
    note_last = 72
    sm_th = 10
    
    period_1 = 12800
    period_2 = 6400
    period_3 = 6400
    
    T_base = 1600
    T_base_3 = 800

# AB
    while (tick < period_1):
        tick_round = tick%12800
        if tick_round < T_base:
            chord = chorus_a_1
            scale = scale_1
        elif T_base <= tick_round < T_base*2:
            chord = chorus_a_2
            scale = scale_2
        elif 3200 <= tick_round < 4800:
            chord = chorus_a_3
            scale = scale_3
        elif 4800 <= tick_round < 6400:
            chord = chorus_a_4
            scale = scale_4
        elif 6400 <= tick_round < 8000:
            chord = chorus_a_1
            scale = scale_1
        elif 8000 <= tick_round < 9600:
            chord = chorus_a_2
            scale = scale_2
        elif 9600 <= tick_round < 11200:
            chord = chorus_a_3
            scale = scale_3
        elif 11200 <= tick_round < 12800:
            chord = chorus_a_4
            scale = scale_4
        
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(100,chord[0]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 50]),\n".format(0,chord[1]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 50]),\n".format(0,chord[2]))
        
        onset = rand.random()
        if onset > 0.3:
            note = pt.gen_next_note(scale[0],mode)
            note = smooth.smooth(note, note_last, sm, sm_th)
            note_last = note
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(0,note))
        else:
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 0]),\n".format(0,note))
        
        onset = rand.random()
        if onset > 0.5:
            note = pt.gen_next_note(note,mode)
            note = smooth.smooth(note, note_last, sm, sm_th)
            note_last = note
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(100,note))
        else:
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 0]),\n".format(100,note))
        

        onset = rand.random()
        if onset > 0.4:
            note = pt.gen_next_note(note,mode)
            note = smooth.smooth(note, note_last, sm, sm_th)
            note_last =  note
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(100,note))
        else:
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 0]),\n".format(100,note))

        onset = rand.random()
        if onset > 0.5:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        tick = tick + 400
    
    
    note_last = 72
    sm_th = 9
    tick = 0
    # bridge
    while (tick < period_2):
        tick_round = tick%period_2
        if tick_round < T_base:
            chord = chorus_b_1
            scale = scale_1_b
        elif T_base <= tick_round < T_base*2:
            chord = chorus_b_2
            scale = scale_2_b
        elif T_base*2 <= tick_round < T_base*3:
            chord = chorus_b_3
            scale = scale_3_b
        elif T_base*3 <= tick_round < T_base*4:
            chord = chorus_b_4
            scale = scale_4_b
    
        
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(100,chord[0]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 50]),\n".format(0,chord[1]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 50]),\n".format(0,chord[2]))

        onset = rand.random()
        if onset > 0.3:
            note = pt.gen_next_note(scale[0],mode)
            note = smooth.smooth(note, note_last, sm, sm_th)
            note_last = note
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(0,note))
        else:
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 0]),\n".format(0,note))
        
        onset = rand.random()
        if onset > 0.4:
            v = 80
            note = pt.gen_next_note(note,mode)
            note = smooth.smooth(note, note_last, sm, sm_th)
            note_last = note
        else:
            v = 0

        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))

        if onset > 0.3:
            note = pt.gen_next_note(note,mode)
            note = smooth.smooth(note, note_last, sm, sm_th)
            note_last = note
            v = 80
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        else:
            v = 0
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))

        onset = rand.random()
        if onset > 0.5:
            v = 80
            note = pt.gen_next_note(note,mode)
            note = smooth.smooth(note, note_last, sm, sm_th)
            note_last = note
        else:
            v = 0

        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        tick = tick + 400
    
    
    note_last = 72
    sm_th = 9
    tick = 0
    # C
    while (tick < period_3*2):
        tick_round = tick%period_3
        if tick_round < T_base_3:
            chord = chorus_c_1
            scale = scale_1_c
        elif T_base_3 <= tick_round < T_base_3*2:
            chord = chorus_c_2
            scale = scale_2_c
        elif T_base_3*2 <= tick_round < T_base_3*2.5:
            chord = chorus_c_3
            scale = scale_3_c
        elif T_base_3*2.5 <= tick_round < T_base_3*3:
            chord = chorus_c_4
            scale = scale_4_c
        elif T_base_3*3 <= tick_round < T_base_3*4:
            chord = chorus_c_5
            scale = scale_5_c
        elif T_base_3*4 <= tick_round < T_base_3*5:
            chord = chorus_c_6
            scale = scale_6_c
        elif T_base_3*5 <= tick_round < T_base_3*6:
            chord = chorus_c_7
            scale = scale_7_c
        elif T_base_3*6 <= tick_round < T_base_3*8:
            chord = chorus_c_8
            scale = scale_8_c
        
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 70]),\n".format(100,chord[0]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 50]),\n".format(0,chord[1]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 50]),\n".format(0,chord[2]))
        onset = rand.random()
        if onset > 0.3:
            note = pt.gen_next_note(scale[0],mode)
            #note = pt.gen_next_note(note,mode)
            note = smooth.smooth(note, note_last, sm, sm_th)
            note_last = note
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(0,note))
        else:
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 0]),\n".format(0,note))

        onset = rand.random()
        if onset > 0.35:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        
        onset = rand.random()
        if onset > 0.35:
            note = pt.gen_next_note(note,mode)
            note = smooth.smooth(note, note_last, sm, sm_th)
            note_last = note
            v = 80
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        else:
            v = 0
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        
        onset = rand.random()
        if onset > 0.35:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        tick = tick + 400
    
        
#end automatic composing
    fp.write("#end automatic composing\n\n")
    
    
    fp.write("    midi.EndOfTrackEvent(tick=1, data=[])]])\n\n\n")
    fp.write("    midi.write_midifile(\"inception_phase_11_{}_{}.mid\", hh_midi)".format(tone,num))

    fp.close()

    #midi_file = 'inception_phase_11_{}_0.mid'.format(tone)
    #midi_play.play_music(midi_file)



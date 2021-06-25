@namespace
class SpriteKind:
    E2 = SpriteKind.create()
    E3 = SpriteKind.create()
    E1 = SpriteKind.create()
    E4 = SpriteKind.create()

def on_on_destroyed(sprite):
    global k1, k2, k3, K, ms5, p1
    scene.set_background_image(img("""
        ccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaabbaabbbbbbbbaaababaaaaaaaababbbbbbbbbbaaabaaaaaaaaaaabbaaaabbbbbbbbaabbbbbbbbbbbbbfffffffffffcccccccccccccc
                cccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbababaaabbbaaaaababbaabaaabbaaabbaaaaabbbabaaaabbbbbbbbaaaaaaabbbbbbbbbbbbbbbbbbfffcffffffffffcfffcccccfffcc
                cccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbaabbabbbaababbaaabbbbbaabbaaaaaabbaaaaababbbbbbbbbbbafaaaaaaaaaaabbbbbbbabbbbbbbffffffffff111ffcfffcccccfffff
                cccccccccccccccccccccbbbcbbbbbbbbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbabbbaaaaaabaaaaaaaaaaaaaaaaaaafbbbbffafaaaaaffffffffffffffaabbbfffffffdddd11fffccfffffffffffff
                ccccccccccccccccccccbbcbbbbbbbbbbccccbbbbbbbabbbaaaaaabbbbbbbbbbabbbbbbbaaaaaaaaaaaaaaaaaaaaaafffffffffffffffffffffdddfffffffabbffffffddd1111ffccfffffffffffffff
                cccccccccccccccccccbcccccbccbbbbbcccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaafffffddddfffffffffdddddddddddffffffffffdddd1111ffffffffdffffffffffff
                cccccccccccccccccccbbccbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaabbbaaaaaaaaaaaaaaaaaaaaaaaaaffdddd111fffffffdddd11d111111dddfffffddd1111fffffffffddd11ffffffffff
                ccccccccccccccccccccbcbcccccbbbbbbbbbbbbbbbbaabbbaaaaaaabbbaaaaabbaaaaaaaaaaaaaaaaddaaaaaafffff11111bb111ffdddd111111111111d1fffddd1111ffffffffddd111fffffffffff
                ccccccccccccccccccccbbbbbbbcbbbbbbbbbbdddddddddbbbbbbbaaabbbaaaaabaaaaaaaaaaaaaaaddaaaaffffffffffffff1b11ffd111111111111111111ffffff11fffffffddd1111fff1ffffffff
                ccccccccccccccccccbcbcccccbbbbbbbbdddddddddddddddabbaaaabbbbbbaababaaaaaaaaaaaaaaadaaafffaaaaaffffffffbb1ff111111fffff11111111fffffffffffddddddd11ffff1ff1111b1f
                cccccccccccccccccccbccccbcbbbbbbddddddddddddddddddaabbbbaabbbbaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaffffffffff11111111ffccbf111111111fc11ffddddddd11111fff111f11fffbbb
                ccccccccccccccccccccccccccbbbbbdddddddddddddddddddddaaaaaaabbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaffffffff11111111fccbbbf11111111dfcc1111111111111fb11fffffbfff11b
                ccccccccccccccccccccccbbbcbbbbdddddddddddddddddddddddaafffffffabaaaaaaaaaaaaaaaddaaaaaaaaaaaaaaaaaffffdf11111111ffcbbbb11111111ddfc111bbbbbbbbffff1ffffffffff11b
                ccccccccccccccccccccccccccbbfdddddddddddbbbbbbbbddddddffdddddffaaaaaaaaaaaaaaaaddaadaaaaaaaaaaaaaafffdd111111111ffffbb1111111111dfccffffffffffffffffdddd1ff1f11b
                ccccccccccccccccccccccccccbfdddddddddbbbbbbbbbbbbbbbddfdddddddfaaaaaaaaaaaaaaaaadaaadaaaaaaaadaaaffddd111111111111ffffb11111ddddffffcf11ffddddddddddd111ff11f1bb
                cccccccccccccccccccccbbbbcfdddddddbbbbfffffffcccbbbbbfffdddddddfaaaaaaaaaaaddaaaadaadadaaaaaddaaaafddddd1111d11111111ff1111ddfff1111ffffdd111111111111bbf11ff1bb
                ccccccccccccccccccccccbbbfddddddbbbfffffbbbbfffcccbbbfdfffdddddfaaaaaaaaaaaadaaaddaaadcdaaaaddaaaaffffffffffdd11111111f1111d111111111fffd111111111111bbffffff1bb
                cccccccccccccccccccccbbbfddddddbbbfffbbbbbbbbffccccbfddbbfdddddfaaaaaaaaaaaadaaaddddaddddaaaddaaaafffcffcffffffffd11111111111111111111ffffbbbbbb11bbbbf1ffffff1b
                ccccccccccccccccccccbbcffddddbbbffbbbbbbbbbbbbffcccfffddffffdddfaaaaaaaaaaaaaaaaddbddddddddadaaaaaffbbcfcffbcfffffff11111f111111111111111ffffffbbbbfff1ffffff1f1
                cccccccccccccfffccbbcbbfddddbfffbbbbbbbbbbabbbbfcbbffdfdffbfdddfaaaaaaaaaaaddadadbbddbbddddadaaaaaffbbcfccbbcfbfccfffff111fff1111111bb1111ffffffcffffff1ff1fff1f
                cfdcccccccccffdffcbcccfddddffbbbbbffbbbbbbbbbbbffcffdfdfddbffdffaaaaaaaaaaaaaadadbddddbdaaddadaaaaffbfffbcfbcfbfbcfbfff111111111fb111bbb1111ffffffff111111ffffff
                cfdccccccccfffddfcccccfdddffbbbbbfffbbabbbbaaaaffccffdfdffddfdfaaaaaaaaaaaaaaaddaddaddddaaddddaaaaafbfafbffbffbfbcfbcfffff1111111fb111bb11111fffff1f1111111bffbf
                cfdfdccccccffbbdfcccbfddffbbbbbbffffbbbbbbaaaaaffccfffdfdfddfffaaaaaaaaaaaaaaaddaadaddddaadddaaaaaafbfaffffbffbffcfbccffffffff1111ffbbbf11111fffffc1f111111bffbf
                cfdfddcccccffcbdffccbfffbbbbbbbffffdbcbbaabbbbbffcccbffdfffffaaaaaaaaaaaaaaadddddaaaaaadaaadaaaaaaafffafffffffbbfbffbcfcccfffff11111ffff11111ffffff1bb11111bffbf
                ffdffdccccffdbcddfcbbffbbbbbcbffffddbccaaaaaaabfcccbffffffffaaaaaaaaaaaaaaaaddcdaadaaaadaaadaaaaaaaaffaffffffffbfbffbcf11cccffff1111111111111fffffc11bb1111bbbff
                ffdffdccccffdbcddffbbbbbbbbbbbfffddbbbcbbbbaabffccbffffffaaaaaaaaaaaaaaaaaaaddddaaaaaaadaaddaaaaaaaaffafffffffabfffbbcf1f1bcffffff11111111111fffc11111bf1111bbff
                ffdffdccccffdccbdbbbbbbbbbbcbfffddbbccfccaabafffcbfffaaaaaaaaaaaaaaaaaaaaaaaaaddddbaaaaaaadaaaaaaaaaafaffafffaabfffbbffff11bcffffffff1111111fffc1111111f1111bbff
                ffdffdcccfffdbcbdfccbbccfbbbfffddcbbcbfffcbffffccffaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbaabbbbbbbaaaaaaaafafaafffaaffffbbffff111ff111bffff1111fffffff111111bf1111bfb
                fffffdcccffddbcbdfccbbcfbbbfffddcbbbbbbbbbfffcccbfaaaaaaaaaaaaaaaaaaaaaaaaaaabb1111bbbbbb11baaaaaaaaaaafaafffaaffffbfffff1ff11ffffbbfffffffffffff111111bf111bbfb
                fffffdccfffddcccddfbbbbfbbfffddbbbbbbbbffffffccbffaaaaaaaaaaaaaaaaaaaaaaaaaaaccbb11111bbbb1caaaaaaaaaaaaaaafaaaafffbffff11ff1111f1111ffffffbfffff11111bbf111bffb
                cffffdcfffdddcbcddfbbccffffffdbbbbcbbccffddbfffffaaaaaaaaaaaaaaabddaabbdaaaaaacccb11111111caaaaaaaaaaaaaaaaaaaaafffff1f11bffffbf1111fbbbbbb11ffff11111bffc11cffb
                cffffddfffdddccbddffbccfffffddcccbccbffffffdddbdddaaaaaaaaaaaaabbddbbbbddaaaaaacbbbbbb11bbcaaaaaaaaaaaaaaaaaaaaffffffff11bfffff1111f111111111ffff1111bbfffcccf1b
                cfffffdffddddbcbcddfbbfffffdddcbbbcbffffcffffbddddddaaaaaaaaaabbbddbbbbddbaaaaacccccc11bbcaaaaaaaaaaaaaaafaaaaffffffbff1bff11111111f11fff1111ffff111ccfbffcfff1b
                ccfffffffddddccccddfffffffdddccbbbcffbffbcffffdbdddddaaaaaaaacbbbddbbbbddbaaaaaacbccb1cbcaaaaaaaaaaaaaaaffaafaffffffbff1bff111111fffff11f11111ffc1cccffffff111bc
                cccffffffddddccbbbddffffffdccccbbcffbbccbffffffdbddddbaaaaaacbbcbdbbbddbbbaaaaaaccccccbccaaaaaaaaaaaffaaffaafafffffcbfffbf1111fffdd11f111fffffffcccffffffffffccc
                cccfffffdddddbcbbbdddfffffdccccbccfdbbccffbbfffbdddddbbaaaacbbccbbddbbbdddbaaaaaaccbbbbaaaaaaaaaaaaaffaaffafffffbffcbff1ff1111fddd111ffffffffffffffffffffffffffc
                cccfffffdddddbcccbcddfffffdbbbbbbfdbbccbddddbffbdbdddbbaaafbbcccbbddddbbbcdaaaaaaacccccaaaaaaaaaaaaaffaafffbffffbffcbfffff1111dd11111fbbbcccffffffffffffffffffff
                cccfffffdddddbcbcccdddffffbbbbbbbfddbccddddddcffdcbddcbbaffbfffccbbddddbbcbdaaaaaacbbcaaaaaaaaaaaaaafffafffbffffbfbcbbbff111111111fffbbcccccbbffffffffffffffffff
                cccffffddddddccbbcbddddfffdbbbbbfbcdbccbdffbdcffddcdddcbafcbffffcbbdddbdbbcdaaaaaaacacaaaaaaaaaaaaaaffffffffbffbbfbccfff1111f1111fffbbbbcccbbbbbffbfffffbfffffff
                cccffffddddddbcbccbbdddffffdbbbbfbbdbbcfdbfbdbcfddccdddbaffbffffccbbdbbdddbdaaaaaaaaaaaaaaaaaaaaaaaafffffbffbffcbfbffff1111fffffffbbbbbccddddddddbbbbfffffbfffbb
                ccffffdddddddbcccccbddddfffffffffbbddbdcfddbbcfdbdccbddbfffbfffffccbbdddbddddaaaaaaaaaaaaadddddaaaaafffffcffbffccbff111111fffbbbbbbbbbbbdddddddddddbbbbffffffffb
                ffffffdddddddcccbbbbdddddfffffffddbcdbbbfbbbccfdddccbddfffbbfbcfffcbbddbcbddbaaaaaaaaaaadddbbdddbbaafffffccfbbbfcff111111fffcfbbbbbbbbddddddddddddddbbbbfffccfff
                ffffffddddddcfffcccbbdddddfffffbbdbcdddbcfbbffddbbccbddffcbfffbccffcbddcbdddbaaaaaaaaadddbbbcbbddbaafbffffffbbffff111111ffffcfbbbbbbbdddddddddddddddbbbbcfffcffb
                ffffffdddddcccccfbccbdddddfffffbddbbffdbcfffffddbbccbddfffbcffbbcffcddccbdddbbaaaaaaaaddbbccccbddbbbbfffffffffcfff1111ffffffcfbbbbbbbddddddfffcdddddbbbbcfffccfb
                ffffffddddccccccffbcbddddddffffbdbbbbffbbcfbbfdddbcdbddbffbcfffbcffcdccccddbcbbaaaaaabbdbcccccddbbbaaffdd11f11f11dd1ffffffffcffffbbcbdddddffcbbbdddddbbbcfffcccf
                ccffffddddcccccccfbccddddddfffbfdbbffbffbcfbffddbbcdbddcbffbcfffbffcdcccdddbcdddbaaaabbddccccddbbcbaaffdd1dff1111ddffffffffccfccffccdddddffccbfffddddbbbfffffccc
                cfffffddddcccccccfcbbdddddffffbddbbffbcfbbcffffdbccdbddcbfffcffffbfddcdbbdccdddddbaaaabbddddddbccbbbfcffd11ddf1dffffffffffcffbcccfcbdddddffcbbfccddddbbbbffbffcc
                cfffffddddccccccfbccbdddddfffffcddbffbccfbccfffdbcddbbdbcfffbcfbfffddbdbbbbccddddbccaabbbbddbbcccbbffffff111111f11fffdffffffbbbbbcfbddddffccbfccdddddcbbfbbbbbfc
                ffffffdddddcccccfbcbddddddfffccfdddbffbccffccffbbcddbbbccbbbfbfcfbfbdbdbbfccccccbdbdcabbbbbbbbccbbddffddffffffffffffdddddbbbbbbbbcfbddddffcbfcccdddfbccfbbbbbbfc
                ffffffdddddccccffcccdddddffffcfffdddbfffccfccffbccdcbbbcccfffbfcfbfbdcdbcddddccdcbddcccbbcccbdbbbfddbfddddddfffffbfddddddbbbbbbbccfddddddffcbfcfdffffccbbffffbfc
                ffffffdddddccccfbcbbdddddfffcfffffddbbffbccfcffbccdbbbccfcfffbbffcfcdcbbddddddcbddddcacbbbdbbdbfffcdddfdddddddddfbbcddddddbbccbbccfddddddffccbffffffffbbfffffffc
                fffffffdddddccffbcccdddddfffcffffffddbfffbccccfbcbdbbbccccffffbbfcfccccdddddddccbddddcabbbddbddbffccddbffdddddddddbbcbddbcccccbbccffddddddffffffffffbbfffffffffc
                fffffffdddddccfcbcbddddddfffccfffffddbbffffcccfbcbbbbcdccfffffbcbfcfcdddddddbbccbdbdbcaabbdddbdbfffccddbfffbdddddddbccbbcccccccbbccfddbbddddddbffbbbbfffffffffcc
                ffccffffdddddffcbbcddddddffbbcffffffddbbffffbccbbbbccddcccffffbbbfdbbbdbddddddbcccddbcaabddddbdbfffcccdbbffbbbbbdddbcccccccffccbbccfdbbbbbbddbbbbfbbfffffccffccc
                ffccffffdddddcbcbbddddddfffbbccfffffdddbbbfffbcbbbcdddccfffdfffbbffcbbbbddddddbccccdccabbdddbddbbbbfcccdbbdddddbbddbbccccccfffccbccfbbbbbbbbdbbbbbfbfffffccffccc
                ffccfffffddddcbccbdddddfffbbfffccfffcdddbbfffbbbbcddddccfffdfffbdcfdcccbbbdddbcccddcccabbdddbbbbbddffcccbddddddcbbddbbccccffffccbbcffbbbbbbbbbbbfffbffffcccffccc
                fffffffffddddbcccddddddfffbffccddccffbddbbbffbbbcdddddcffffdfffbbdcdccfccbbbbcccbdbccbcbbddbdbddddbddbccddddbbddcbbddbbcccffffcbbbccfcbbbbbbcbbbfffbffffcccffccc
                ffffffffffdddccbddddddffffbfccddddcfffdddbbbfffbdddddccffffddffbbdcfbdfcccccccfcbddbdbcbbddbdbddddddbdcdddbbbfcddbbccdbccffffcbbbbbfffccbbbcbbbbfffbffffcccffccc
                fffffffffffddcbddddddfffffbfcbddddcffffdddbbfffcbddddcffccfddfffbdcdddddddfcffffbdcddbcacbbdbdddddddbdddddbffffcdbbbccbcccfffcbbbbbffccccccbbbbffffbffffcccfffcc
                fffcfbfffffddccddddfffffbfbffcbdddccfffffddbbffcbdddcfffccffdfffbddcbbbddbfffddbcbbbdbcabcbdbdddddddbcdddbfffcccdbbbbcccccfffcbbbbbfffccccccbbbbbffbffffcccfffcc
                ffffffbbffffdbddddffffffbbbfffcbdddccccffddbbffcdddccfffcfffdfffbbdcfcbbbbbfddbbbcbbdfcabcbdbddddddddbddddffccccdbbbbbccccfffcbbbbbfffccccccbbbbbffbfcffcccfffcc
                ffffbbffbfbffffffffffbfbbcfffffcbbddddccfbddbbbccddcffffcfffdffffbdcfffccbcdbbbbfbddccbabcbdbddddddddbcdddffcccddbcbbcbcccfffccbbbbffffccccccfbbbfbbfcffcccffffc
                ffffbbcfbfffbfffffbfbffbfffcffffccbbbdddcbbdbbbccccfffffcffffdfffbddcddddccdbbffcbdbdfbbbdbdbddddddddbcbbdddddddbccbbbcbcccfffcbbbbffffccccccfdddbbbfcffcccffffc
                ffffbbcfbfdbffbfffbbbbbbfffdfcffffcbbddddbbddbbbcccfffffcffffdfffbbddcccfccdbfafcbbdfbcbbdbbbddddddddbcfbddddddbbcbbbbcccccfccccbbbffffcbccccfddddbbfcffccffffff
                ffffbbcfbfddfbfbfbfbbfffffffcfcffffcbbdddfbbddbbccffffffcfffffffffbddcbbcccffaaafcbdddcbddcbbbdddddddbcfbbbbdbbcccfcbbddccccccccbbbffffcbcccbfddddbbfcffccffffff
                cfffbbbcbbcfddfbbfbbbffffccddfccdfffcbdddccbddbbccffffffcfffffbfffbcddcbbcffaaaafcbbddbbddddcddddddddbcffbbbbbccccbcbbddccccccccbbbfffcccbccbfbdddbbffffccffffff
                cfffffbcbbcccdbbbbfcbfffccfbdbffcdfffcbddcccbdbbccfffcffccffffbfffbcddcfffffaaaafffbddcbdddddbbdddddbbccfffbfccccbbccbbddcccccccbbbfffccbbccbbfbddbbffffccffffff
                cfffffbbcbcfcddbbcfccfccbbffbfbffcccfcbbddccbddbbcfffcffcccfffbffffbcbdcffffcaafffbbddbbbddddcbbdddbbcccfffffcccbbbbcbbbddccccfcfbffffccbbbccbfbbdbbfffffcffffff
                cfffffbbccffccdbbccfccfbddfffddbfcddfcbbddccbbddbccfffccfccfffbdfffbccdcffffcffdddbbbdcbbbddddbbbbbbbccfffffccccbbbbccbbddddccffffffffccbdbccbbcfbbbbfffffffffff
                cffffbfbcffffdbbbcffccfbdddffddcfdddffcbddccbbddbbccffffffcfffbdfffbbcddcfcbbffdbbbbddcdbbddddcbbbbbcccfffffccccbbbbcccbbdddddcffffffffcddbbbcbfbbbbbfffffffffff
                ccfffbfbcffffdbbcffffcffcbddfcbfdffdbfcbddcccbbddbbcffffffcffffdffffbccdbcbbcfdbfbbbdbcddbbdddddcbbbccffffffccccbbddbccbbdddddcccffffffcddbbbccbcfbddfffffffffff
                ccfffbfbbcfffdbbcffffcffbbddfffbdbbfcfccbdcbcbbddbbbccfffccffffddfffbdcddbcccfffffbdbbcbdbbddddddccccccfffffccccbdddbbccbddddddcccfffffcbddbbbcccfbddbffffffffff
                cccffbfddcfffcbbccfffcfffbbbdffdddcffcfcbdcbbbbbddbbbccccffffffbdfffbbccddcccccfffbdbcbbddbbdddddbbbccffffffccccbddddbccbbdddddddccffffcbddbbbbbccbbddbbffffffff
                cccffbbddbcffcbbbcfffccffbbbddfffdccffffcdcbbcbbbddbbbbccffffffbbdfffbcccdbcccfbbddbbcbbbdbbbbddddbbbcfffffccccbbddddbcccbbddddddccffcccbbddbbbbbcbbbddbbfffffff
                cccffffbddbcfcdbbcffcbcffffbbdfffbccffffcdccbccbbbddbbbbcfffffffbdfffbdccdbcccffbbbbccbbbddbbbbdddbbbccfffccccccbddddbbccbbdddddddccfcccbbcddbbbbbcbbbddbbbbbfff
                ccccfffbfddccbdbbcfccfcffffffbbdfffffffffdccbbccbbbddbbbcffdffffbdfffbbccddfccccfffffcbbbdddcbbbddbbbcccccccccccbdddddbccbbbdddddddcffccbbccdddbbbccbbbbbbbbffff
                cccffffbffdbcdddbbccbfccffffffbbffffffffffdcbbcfbbbbdbbbcffdffffbdffffbcccdffccbcccccdbbbddddcbbbbbbcccffffcccccbdddddbbcbbbbddddddbcfccbbbbccdbbbbcccbbbbbbffff
                cccffffbbcdbccdddbcbbbbbcfffffbdddbbddddffccbbbbfbbbddbbcffdffffbddfffbdcccdffccbccccdbbbdddddcbbbbcfcffffffccbbbbdddddbcccbbbbdddbbcfccbbbbbcddbbbbbccbbbbbffff
                cccfffffbcddccddbbbfbbbbbcffffffbbbbbbbbddddcbdbbcffbfdbcfffdfffbbdfffbdccddbffcbcccbbdbbcdddddcbbbbcfffffffccbbbbdddddbbcccbbbbbbbbbfccbbbbbbcddbbbbbcccbbbffff
                ccccffffdccdbccddbbbfbbbbbcffffffccccccbddddccbddbbbbfcdccffdfffbbdcfffbdccdbbffbcccbbbdbcbbddddccbbbcffffffccbbbbbdddddbcccbbbbbbbbbffcbbbbbbbdddbbbbcccccfffff
                ccccffffddcdbcccdbbbbfbbbbcfffffcfffccccccfcccbdddbcbbccccffdffffbdccffbddcddbbfbcccbbbddbcbbddddccbbfcfffffcccbbbbbddddbbbccbbbbbbbcffcdbbbbbbcdddbbbbbccccffff
                cccccfffbddddccccdbbbcffccffffffccffffcccccccccbdddbdbbbccbfdffffbbdcfffbdccddbfbccbbbbbddbcbbddddccbbfcffffccccbbbbbbdddbbbccbbbbbbcfffcdbbbbbbcdddbbbbbbcccfff
                cccccfffbddddbbcccddbbbffcffffffccccfffbbdccbccccddddbbbccbfdffffbbdcccfbdbccddbfccbbbbbddddcbbddddcccffcfffccccbbbbbbbdddbbbcbbbbbbcfffcddbbbbbcbbdbbbbbbbccfff
                ccccfffffdbccdbcccdddbbbfcfffffcccbcccccbdbcbccbcbdddccbbcbbddfffbbddccfbbbcccdfbccbbbbbbdddccbbbbbdddcffcfccccccbbbbbbbdddbbccbbbbbcfffcddbbbbbbcbddbbbbbbbcccf
                cccfffffffcccddbcccddbbbbcfffffccccbbcccbbdcbbbcbbbdddbbbcbbddffffbddccffdbcccddfccbbbbbbddddcbbbbbbbdfcfcccccccccbbbbbbbdddbbccbffbffffcbddbbbbbccbdddbbbbffccf
                cccffffbfffccddbbbccddbbbfcfffffcbcccccccbdcbbbbccbbddbbbcbbbdcfffbbddccffddbccdfccbbbbbbbdbdddcbbbbbbbfffffcccccccbbbbbbbddbbcccfffffffcbdddbbbbcccdddbbbbffccc
                cccffffffffcccddbbbccddbbfcfffffcbbbcccccbbcdbbcffcbdddbbccbbddcffbbdddccffbbccdffcbbccbbbbdddddccbbbbbfffccccccccccbbbbbbbddbbfccffffffbbddddbbbbbcccdddbbfffcc
                cccffffbbbffdccdbbbbcfbbbfcfffffcdbbbbcccbbbddbbcffbbbddbbccbbdcfffbbddcccccdcccbfbbbbcbbbbbdddddccbbbbbfffcccccccccccbbbbbbdbbfffcfffffbbbddddbbbbccccbdbbffffc
                ccffffffbbfffdccddbbbfbbbfcffffcfbddbbbccbbbbcdbbcfffbbdbbbcbbdccfffbdddccccbcccbfbccbbcbdbbbdddddcccbbbbfffccbccccccccbbbbbbdbbfffcfffcbbbbddddbbbbbbcfffffffff
                fffffffccbbffffcddddbbcffcfffffcbbbccbbcccbbbbfdbbcffffbbbbbcddcccffbbdddccccbccbfbcbbbccbdbbdddddddccfffffffcbddbbbccccbbbbbbbbbffcfffcbbbbbcddddbbbbccffffffff
                ffffffffcdbbffffccdddbbbffcffffccbbbbcccccbbbcffbbbbcffffbbbbcddcccfbbbddccccbcccbccbbcbcbbdbbddbdddddfffffffbbdddddbcccbbbbbbbbbffcccccbbbbbcdddddbbbfcffffffff
                ffffffffcdbbbffffcccddbbfcffffffcbbbbbbccccbbcfffbbbbcffffbbbccddcccfbbbddcccbbfccccbcccbccbbbcdbbdddfffffffcbbbdddddbcccbbbbbbbffffccbbbbbbbbcdddddbbffcfffffff
                ffffffbfccdbbbfffffccddccfffffffcdbbbbbbccdccccfffbbbbcffffbbbdddcccccbbddfcccbffccbbcccccccdbbcbbbbfffffffccbbbbbddddbbccffbbbfffffccbbdbbbbbbcdddddbfffcffffff
                fffffffffcdddbbbffffffccfffffffffcdbbbbbbcccddcccfffbbbcffffbbcddccccccbbbbffccbccbbcccdcbbccbbbccffffffffccccbbbbbbbbbbcccfffffffffccbbdddbbbbcddddddbfffcccfff
                fffffbfffccdddbbbbfffffcfffffffffcddbbbbbbcccdddcccfffbccfffccfcdddccccccbbbffccccbccdddbbbbccbbbbccfffffffcccbbbbbbbbbbbcccffffffffccbbdddddbbccdddddbfffffcccf
                ffffccfffffcdddbbbbbbffffcfffffffffcbbbbbbbbcccddfccccccfcccccffbddbccccccbbbffccbbcdddbbcbbbccccbcccffffffcccbbbbbbbbbbbbcccccfffccccbbbddddbbcccffdddffffffffc
                ffffcfffcffffddddddbccccccffffffffffcdbbbbbbbbcccdfffcccccfccccfbbdbbcccccbbbbfffbbcbbbbbcbbbbccccccffffffffccbbbbbbbbbbbbcccccccccccccbbbbdddbbcccfffffffffffff
                fffccfccbbccfffccccccbdddbcfffffffffffddbbbbbbbcccdfffffbbcccccffbbdbbbccbcccffffbccbbccccbbbbbcccccfffffffbbbbbbbbbbbbbbbbcccccfcccccccccbbbbbbffccffffffffffff
                fffbbbccbbbbcccfcbbbbbbddddffffffffffffdddbbbbbbcccccccccccffcccffbbbbbcccbffbbffbccccccbbbbbbffcccccfffffcbbbbbbbbbbbbbbffffccffffcccccfccbbbbbfffccfffffffffff
                ffbcfcccdbbbbbbcccbbbbbbbdddffffffffffffffbbcccccccccccccffffffccfffbbbbcccbfffffccccccbbbbbbfffffcccccffcccfffbbbbbbbbbfffffccccccccccccccccbbffffcccccffffffff
                ffccccfccdbbbbbbbcbbbbbbbbbddccfffffffffffffccffffffffffffffffffccccccccccccccffcccccccbbbbfffffffcccccccccccfffffbbbffffffffffccccccccccccccffffffffffccfffffff
                fccccfffcdddbbbbbffccbbbbbbbdbcffffffffffffcffffffffffffffffffffffffffccccccccccccccccccbbbffffffffffccccccccccfffffffffffffffffffccccccccccccffffffffffccffffff
                cccfffffcccddbbbbcfffcccbbbbbbcccffffffffccffffffffffffffffffffffffffffffccccfffffffffffcccfffffffffffccccccffcccccffffffffffffcccccccccccccccccffffffffffffffff
                ccfffffffffcdddbbcccfffccccccccffccffffffcffffffffffffffffffffffffffffffffcccffffffffffffccccfffffcccccccccffffffccccccfffffffccfccfffffffccccccccccffffffffffff
                ffffffffffffccccccccfffffffffffffffccccccfffffffffffffffffffffffffffffffffffffffffffffffffffccccccccccccfffffffffffffccccfffcccccfffffffffffffccccccccffffffffff
                ffffffffffffffffcccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccffffffffffffffffffcccccccfffffffffffffffffffffffccccfffffff
                ffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccccfcc
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccc
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    """))
    k1 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . f f f f f f f . . . . 
                    . . . . f 1 1 1 1 1 1 f f f . . 
                    . . . . f 1 1 1 1 1 1 1 1 f f . 
                    . . . . . f 1 1 1 1 1 1 1 1 f . 
                    . . . . . f f f f f 1 f 1 1 f f 
                    . . . . . f f 1 1 1 1 1 1 1 f f 
                    . . . . . . . f 1 1 1 1 1 b f f 
                    . . . . . . . f f f 1 1 1 b f f 
                    . . . . . . . . . f f f b f f f 
                    . . . . . . . . . . . f f f f f 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.food)
    k1.set_position(48, 42)
    k2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . f f . . . . . . . . . . . 
                    . . f 1 1 f . . . . . . . . . . 
                    . . f 1 f f . . . . . . . . . . 
                    . f 1 1 1 f f . . . . . . . . . 
                    . f 1 1 1 1 1 f . . . . . . . . 
                    . f 1 1 1 1 b f . . . . . . . . 
                    . f 1 1 1 b f f . . . . . . . . 
                    . f b b b f f . . . . . . . . . 
                    . . f f f . . . . . . . . . . . 
                    . . f . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.food)
    k2.set_position(82, 35)
    k3 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . f f f f f . . . . . . 
                    . . . f f f 1 1 1 f f f . . . . 
                    . . . f 1 1 1 1 1 1 1 1 f f f . 
                    . . f f 1 1 1 1 1 1 1 1 b f f . 
                    . . f f 1 1 1 1 1 1 b b f f f . 
                    . . . f f 1 1 b b b f f f f . . 
                    . . . . f f f f f f f f f . . .
        """),
        SpriteKind.food)
    k3.set_position(132, 41)
    game.show_long_text("茉莉:把碎片合起來吧", DialogLayout.BOTTOM)
    k1.destroy()
    k2.destroy()
    k3.destroy()
    pause(1000)
    K = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . f f f f f f f . . . . 
                    . . . . f 1 1 1 1 1 1 f f f . . 
                    . . . f f 1 1 1 1 1 1 1 1 f f . 
                    . . f 1 1 1 1 1 1 1 1 1 1 1 f . 
                    . . f 1 f 1 f f f f 1 f 1 1 f f 
                    . f 1 1 1 1 1 1 1 1 1 1 1 1 f f 
                    . f 1 1 1 1 1 1 1 1 1 1 1 1 f f 
                    . f 1 1 1 1 1 1 1 1 1 1 1 b f f 
                    . f 1 1 1 1 1 1 1 1 1 1 b f f f 
                    . f 1 1 1 1 1 1 1 1 1 1 b f f f 
                    . . f 1 1 1 1 1 1 1 1 1 b f f . 
                    . . f f 1 1 1 1 1 1 1 b f f f . 
                    . . . f f 1 1 b b b f f f f . . 
                    . . . . f f f f f f f f f . . .
        """),
        SpriteKind.food)
    game.show_long_text("茉莉:完成!", DialogLayout.BOTTOM)
    K.destroy()
    ms5 = sprites.create(assets.image("""
        11
    """), SpriteKind.E4)
    ms5.set_position(124, 89)
    p1.destroy()
    game.splash("遺跡的門被打開")
    game.splash("在長廊的黑暗處")
    game.splash("聽見了劇烈的聲音")
    game.splash("「碰！碰！碰！」")
    game.splash("那巨大的影子外型")
    game.splash("比剛剛的鈣王還更粗壯")
    game.splash("「人類」")
    p1 = sprites.create(img("""
            ................................................
                    ...................fffffffffff..................
                    ..................fbbbbbbbbbbff.................
                    ..................fbbbcbccbcbbf.................
                    .................ffbbbbbbbbbffffffff............
                    .................fbbbbbbbcffbbbbbbbffff.........
                    .................fcbbbbbcfbbccccccccbbf.........
                    .................fccccccfbcccccccccccff.........
                    ..............ff6ffffffffffffffffffff...........
                    .............ff9ffefbbbffffbbfffff..............
                    .............f49fefdddd1ffddd1ffdf..............
                    .............f49ffffddd1ffddd1ffdf..............
                    .............f4496ffdddd33ddddd3ff..............
                    .............f44eefffdddddfddfddf...............
                    ........ff.ff44eeeefffddddfffddff...............
                    ........ffff44eeeeeeffffddddbfff................
                    .........ffffeeeeeeffffffddbf...................
                    ............ffeefffffff6ffdbffffff..............
                    .............ffffff44f966ffff6ff44ff............
                    ...............ffff455f6999ff669f4fff...........
                    ..............ff999f555f699fff966ff9f...........
                    ............ff999999f55f66669ff969fff...........
                    ...........ff9999966f44f9669999f999fff..........
                    ..........f999966666f44f99999f9f999f6ff.........
                    ..........f9996666fff44f9999999f966f99ff........
                    ..........f99966ffeffef999999f9f66ff6999f.......
                    ..........f9996ffeeeff669996669f6f.ff699f.......
                    ..........f99999fffefff666666fffff..ff699f......
                    ..........ff666999fefffffffffffccf.ff6999ff.....
                    ...........ff66669ffffffccccccccbf.f666999f.....
                    ............ff66fffdffccccccccccbfff66699ff.....
                    .............ffffdddfffccccccccbbfff6699ff......
                    ...............fddddffccccccccbbbffd669ff.......
                    ............ffffdddbffffffffffffffbdffff........
                    ............fdddddbfcfccbbbbbbbfffbddf..........
                    ............ffbbbbffcbcbbbbbbbbbbbfbddf.........
                    .............ffffffcbccbbbbbbbbbbbffbbf.........
                    ..............fffffcbcbbbbbbbbbbbbbffff.........
                    ................fccbccbbbbbbbbbbbbbfff..........
                    ................fcccccbbbbbbbbbbbbbbbf..........
                    ................fcccbbbbbbbffffbbbbbbbf.........
                    ................fccbbbbbbbbfffcbbbbbbbbf........
                    ................fccbbbbbbbbffccbbbbbbbbff.......
                    ................fcbbbbbbbbbfffccbbbbbbbbf.......
                    ................fbbbbbbbbbbf.ffcbbbbbbbbf.......
                    ................fbbbbbbbbbff..fccbbbbbbbbf......
                    ...............ffbbbbbbbbff...ffccbbbbbbbf......
                    ...............fbbbbbbbbff.....ffcbbbbbbbbf.....
        """),
        SpriteKind.player)
    p1.set_position(16, 64)
    game.show_long_text("茉莉：「欸不是..", DialogLayout.BOTTOM)
    game.show_long_text("是不是哪裡搞錯了?」", DialogLayout.BOTTOM)
    game.show_long_text("史萊姆王：$*-？、！", DialogLayout.BOTTOM)
    game.show_long_text("茉莉：What？", DialogLayout.BOTTOM)
    game.show_long_text("史萊姆王：$@.。！", DialogLayout.BOTTOM)
    game.show_long_text("茉莉：講人話拜託", DialogLayout.BOTTOM)
    game.show_long_text("史萊姆王：#%*&#？", DialogLayout.BOTTOM)
    game.show_long_text("（看起來對於我們", DialogLayout.BOTTOM)
    game.show_long_text("聽不懂他說什麼感到生氣）", DialogLayout.BOTTOM)
    game.show_long_text("茉莉：怕講話卡其哪啊？", DialogLayout.BOTTOM)
    game.show_long_text("算了打倒你就對了", DialogLayout.BOTTOM)
    p1.destroy()
    p1 = sprites.create(img("""
            ................................................
                    ...................fffffffffff..................
                    ..................fbbbbbbbbbbff.................
                    ..................fbbbcbccbcbbf.................
                    .................ffbbbbbbbbbffffffff............
                    .................fbbbbbbbcffbbbbbbbffff...f.....
                    .................fcbbbbbcfbbccccccccbbf...ff....
                    .................fccccccfbcccccccccccff..f1ff...
                    ..............ff6ffffffffffffffffffff....f11f...
                    .............ff9ffefbbbffffbbfffff......ff15f...
                    .............f49fefdddd1ffddd1ffdf......f15ff...
                    .............f49ffffddd1ffddd1ffdf......f15f....
                    .............f4496ffdddd33ddddd3ff.....ff15f....
                    .............f44eefffdddddfffdddf......f15ff....
                    ........ff.ff44eeeefffddddffdddff.....ff15f.....
                    ........ffff44eeeeeeffffddddbfff......f155f.....
                    .........ffffeeeeeeffffffddbf.........f155f.....
                    ............ffeefffffff6ffdbffffff...ff55ff.....
                    .............ffffff44f966ffff6ff44ff.f155f......
                    ................fff455f6999ff669f4ffff15ff......
                    ...............ff99f555f699fff966ff9ff55f.......
                    ...............f9999f55f66669ff969fff15ff.......
                    ...............f9999f44f9669999f999ff55f........
                    ...............f9999ff4f99999f9f999f15ff........
                    ...............ff9996fff9999999f96ff15f.........
                    ................f699996f99999f9f6fff5ff.........
                    ................ff999996f996669f6f155f..........
                    .................f6999999f666fff9f155f..........
                    .................ff699996ffff999f155ff..........
                    ..................ff6996999ff999f155ff..........
                    ...................ff6999999f99ff15f6f..........
                    ....................fff99999ffff155f6f..........
                    ...................fffff999ffffff5ff6f..........
                    ...................ffccff9ffddfffff6f...........
                    ...................fccccfffddddfffff............
                    ..................ffcbccffdddddddfbf............
                    ..................fcbccbffddddddffbf............
                    .................ffcbcbbbffbddbffbbf............
                    ................fccbccbbbbffbbffbbbbff..........
                    ................fcccccbbbbbfffbbbbbbbf..........
                    ................fcccbbbbbbbfffbbbbbbbbf.........
                    ................fccbbbbbbbbffcbbbbbbbbbf........
                    ................fccbbbbbbbbffccbbbbbbbbff.......
                    ...............ffcbbbbbbbbbfffccbbbbbbbbf.......
                    ...............ffbbbbbbbbbbf.ffcbbbbbbbbf.......
                    ..............fffbbbbbbbbbff..fccbbbbbbbbf......
                    ..............fffbbbbbbbbff...ffccbbbbbbbf......
                    ..............ffbbbbbbbbff.....ffcbbbbbbbbf.....
        """),
        SpriteKind.player)
    p1.set_position(16, 64)
    game.splash("請選擇攻擊武器")
    mySprite.say(game.ask("a水槍 b帽子"))
    if controller.B.is_pressed():
        game.show_long_text("茉莉使用香蕉皮", DialogLayout.BOTTOM)
        game.show_long_text("史萊姆王滑倒", DialogLayout.BOTTOM)
        game.show_long_text("史萊姆王使用文字亂碼", DialogLayout.BOTTOM)
        game.show_long_text("茉莉問號", DialogLayout.BOTTOM)
        game.show_long_text("最後一擊茉莉使用帽子", DialogLayout.BOTTOM)
        game.show_long_text("史萊姆王爆炸", DialogLayout.BOTTOM)
        ms5.destroy()
        p1.destroy()
        p1 = sprites.create(img("""
                ................................................
                            ...................fffffffffff..................
                            ..................fbbbbbbbbbbff.................
                            ..................fbbbcbccbcbbf.................
                            .................ffbbbbbbbbbffffffff............
                            .................fbbbbbbbcffbbbbbbbffff.........
                            .................fcbbbbbcfbbccccccccbbf.........
                            .................fccccccfbcccccccccccff.........
                            ..............ff6ffffffffffffffffffff...........
                            .............ff9ffefbbbffffbbfffff..............
                            .............f49fefdddd1ffddd1ffdf..............
                            .............f49ffffddd1ffddd1ffdf..............
                            .............f4496ffdddd33ddddd3ff..............
                            .............f44eefffdddddfffdddf...............
                            ........ff.ff44eeeefffddddffdddff...............
                            ........ffff44eeeeeeffffddddbfff................
                            .........ffffeeeeeeffffffddbf...................
                            ............ffeefffffff6ffdbffffff..............
                            .............ffffff44f966ffff6ff44ff............
                            ................fff455f6999ff669f4fff...........
                            ...............ff99f555f699fff966ff2f...........
                            ...............f9999f55f66669ff969ff2...........
                            ...............f9999f44f9669999f999fff..........
                            ...............f9999ff4f99999f9f999f6fff........
                            ...............ff9996fff9999999f966ffddff.......
                            ................f699996f99999f9f66ffffddf.......
                            ................ff999996f996669f6f9f9fddf.......
                            .................f6999999f666fff99999fddf.......
                            .................ff699996ffff99999999fddf.......
                            ..................ff6996fff999999999ffff........
                            ...................ff69999999999999fff..........
                            ....................fff9999999999ffff2f.........
                            ...................ffcf6999999fffff922f.........
                            ...................ffccf699666fcccf922f.........
                            ...................fccccf666ffccccf922f.........
                            ..................ffcbccfffffcccbbf992f.........
                            ..................fcbccbbbbbbbbbbbf992f.........
                            .................ffcbcbbbbbbbbbbbbbf9ff.........
                            ................fccbccbbbbbbbbbbbbbfff..........
                            ................fcccccbbbbbbbbbbbbbbbf..........
                            ................fcccbbbbbbbffffbbbbbbbf.........
                            ................fccbbbbbbbbfffcbbbbbbbbf........
                            ................fccbbbbbbbbffccbbbbbbbbff.......
                            ...............ffcbbbbbbbbbfffccbbbbbbbbf.......
                            ...............ffbbbbbbbbbbf.ffcbbbbbbbbf.......
                            ..............fffbbbbbbbbbff..fccbbbbbbbbf......
                            ..............fffbbbbbbbbff...ffccbbbbbbbf......
                            ..............ffbbbbbbbbff.....ffcbbbbbbbbf.....
            """),
            SpriteKind.player)
        p1.set_position(16, 64)
        game.show_long_text("史萊姆王：掰...掰..", DialogLayout.BOTTOM)
        game.show_long_text("茉莉：...算了", DialogLayout.BOTTOM)
        game.show_long_text("starts戰利品", DialogLayout.BOTTOM)
        game.show_long_text("open模式", DialogLayout.BOTTOM)
        game.show_long_text("(記得要大聲喊)", DialogLayout.BOTTOM)
        game.splash("茉莉打開寶藏")
        game.show_long_text("茉莉：什.....什麼！", DialogLayout.BOTTOM)
        game.splash("是續集！")
        game.splash("本篇以完全結束")
        game.splash("敬請期待下一個作品")
        game.splash("感謝各位的遊玩")
        game.over(True, effects.confetti)
    else:
        game.show_long_text("史萊姆王:哈哈", DialogLayout.BOTTOM)
        game.show_long_text("你已死亡", DialogLayout.BOTTOM)
        game.show_long_text("請重新遊玩", DialogLayout.BOTTOM)
        game.reset()
sprites.on_destroyed(SpriteKind.E3, on_on_destroyed)

def on_on_destroyed2(sprite):
    global ms4, p1
    scene.set_background_image(img("""
        1111111111bbbccffffffff111111111bbccffffffff11111111bbbbbfffffffffff11111111111bbccffccccccccff11111111111bbcccfffcccfff1111111111111111111111111111111111111111
                1111111111bbccfffcfff11111111111bccffffccfff11111111bbbcccffffffffff11111111111bccffcccccccff111111111111bbccfffcccccff11111111111111111111111111111111111111111
                111111111bbcfffcccfff11111111111bccffccccff111111111bbbccffffccccfff11111111111bcfffccccccff111111111111bccffffccccccf111111111111111111111111111111111111111111
                111111111bcffffccccf111111111111bcffcccccf111111111bbbbccffcccccccff11111111111bcffcccbbccff11111111111bbccfffcccbccff111111111111111111111111111111111111111111
                111111111bcfffccbbcf11111111111bbcffcccbcf111111111bbbccfffcccbbccff11111111111bcffccbbbbcff11111111111bccffffcbbbcfff111111111111111111111111111111111111111111
                11111111bbcffcccbbcf11111111111bccfccbbbcf111111111bbbccfffcbbbbbcf11111111111bbcffcbb11bff111111111111bbcfffcbb11cfff111111111111111111111111111111111111111111
                11111111bccffccb1bcf11111111111bcffcb11bcf1111111111bbccffcbbb11bbf11111111111bcfffcb111bff1111111111111bcfffcb11cfff1111111111111111111111111111111111111111f11
                1111111bbcfffcb11bcf11111111111bcffcb11bcf1111111111bbccffcbb1111bf11111111111bcfffcb111bff1111111111111bcfffcb11cfff1111111111111111111111111111111111111111fbb
                1111111bbcfffffffcff1111111111bbcfffffffff1111111111bbcfffbb11111ff1111111111bbcffffff111ff1111111111111bcfffcbbbcfff1111111111111111111111111111111111111111fcc
                111111bbcfffffffffff1111111111bccff66666ff1111111111bbcffbbffff11f11111111111bbcfffffffffff111111111111bbccffccffffffb11111111111111111111111111111111111111bbfc
                111111bbcfff66666ff11111111111bcfff666666ff1111111111bcfffff666f1f11111111111bbcffff6ffffff111111111111bccccff666ffffb111111111111111f111111111111111111111bbcfc
                111111bccff666666ff11111111111bcf66666666ff1111111111bcfff66666fff11111111111bbcff66666ffff111111111111bccff6666fffbb111111111111111ffb11111111111111111111bccfc
                11111bbcfff666666f11111111111bbff666666666f1111111111bcff6666666ff11111111111bcff6666666fff111111111111bccf66666fff11111111111111111ffb11111111111111111111fccfc
                11111bcfff6666666f11111111111bcff666666666f1111111111bcff66666666f11111111111bcf6666666666f111111111111bccf66666fff111111111111111111fcb1111111111111111111fcfff
                1111bbcff6666666f111111111111bcff666666666f1111111111bcff66666666f1111111111bbcf6666666666f111111111111bccf666666ff111111111ff1111111ffbb111111111111111111fcfff
                1111bcfff6666666f11111111111bbcff666666666ff111111111bcf666666666f111111111bbcff666666666ff11111111111bbcff666666ff1111111111ffbb1111ffcbb11111111111111111fcfff
                111bbcfff6666666f1111111111bbcff6666666666ff111111111bcf666666666f111111111bccff666666666ff11111111111bbcf6666666ff1ffff111111ffcb1111fffbb111111111111111fcfcff
                111bbcfff666666f11111111111bcff66666666666ff111111111bcf666666666f11111111bbccff666666666f111111111111bccf666666ff11bccf11111111fccb111ff1111111111111111bfcffff
                11bbcffff666666f11111111111bcff66666666669ff111111111bcf66666666ff11111111bbcfff666666666f111111111111bccf666669ff111bcff11111111ffbf11111111111111111111bfcffff
                11bbcfff6666666f1111111111bbcf6666666666699f111111111bcf66666666ff11111111bccff666666666ff111111111111bccf666669ff111bffff111111111111111111111111111111bfffffff
                1bbbcfff6666666f1111111111bccf6666666666699f111111111bcf66666666ff11111111bccff666666666ff111111111111bccf6666699f111fffffff1111111f1111111111111111111bf1ff1fff
                1bbccfff666666ff1111111111bccf666666666699f1111111111bcf66666669f111111111bcff6666666666f1111111111111bccf6666999ff11fffffffff11111ff11111111111bbbbbbbfc1ff1fff
                1bbcfff6666666f1111111111bbccf666666666999f1111111111bcf6666666ff111111111bcff6666666666f1111111111111bcff66669999f11fffffffff11111ff1111bbffffffffffffff1111fff
                bbbcff66666666f1111111111bccff666666669999f111111111bbcf6666669ff111111111bcf66666666666f1111111111111bcf6666999999f1ff2fffffb11111ff111fffffffcccbb11111ff11fff
                bbcfff6666666ff1111111111bccff666666669999f111111111bccf6666699ff111111111bcf6666666666ff1111111111111bcf6666999999f11f22ffffb1111111111ffffffccbbb111111111fff6
                bbcfff6666666ff1111111111bccf6666666699999f111111111bcff6666699f111111111bbcf9666666666ff1111111111111bcff6669999999f1122ffff11111111111ffffffbbb11111111111ff66
                bbcfff666666fff111111111bbccf6666666999999f111111111bcff6666699f111111111bbcf9666666666f11111111111111bccf666999999ff11fffffb111b1111b111ff1ffb1111111111fffff66
                bbcff6666666ff1111111111bcccf666666699999f111111111bccf66666699f111111111bccf9666666666f11111111111111bccf666999999ff11fffff11111bbbbb111ff1ffb1111111ffffff6666
                bbcff6666666ff1111111111bcccf666666699999f111111111bccf66666699f111111111bcff9666666666f11111111111111bccf669999999ff1111111111111bbbb11fff1fbfffffffffbfff66666
                bccf66666666f11111111111bcccf666666699999f111111111bccf66666699f111111111bcff9666666666f11111111111111bcff66999999ff111111111ffff1111111fcfffffcccccccbbbbff6666
                cccf66666666f11111111111bccff666666699999f111111111bccf6666669ff111111111bcff9666666666f11111111111111bcf66699999fff111111111bbffff1f11fccffffccbbbbbbbbbfbf6666
                ccff66666666f1111111111bcccf6666666999999f11111111bbccf6666699ff111111111bcf99666666666f11111111111111bcf66699999fff1111111111fb1ffffffcccffffcbbbbbbbbbfbfff666
                ccf666666666f1111111111bcccf6666666999999f11111111bccf66666699f1111111111bcf99666666666f11111111111111bcf666999999ff1111111111ff1ffcffccfbbfffcbbb11111bfbccf666
                cff666666669f1111111111bcccf666666699999f111111111bccf66666699f1111111111bcf99666666666f11111111111111bcf666999999ff11f11111f1bf11ffbfbbf11bffbbb1111bbbbbffffff
                fff666666669f1111111111bcccf666666699999f111111111bcff66666999f1111111111bcf99666666666f11111111111111bcf666999999fff11f1111bf1bffff1bb1f111ffffb1111b11bcffcffb
                ff6666666699f1111111111bccff666666699999f11111111bbcf666666999f111111111bbcf99666666666f11111111111111bcf666999999f1ffff1fff1bfffbbfff11f111ff6fff11bf1bbfffcffb
                f66666666999f1111111111bccff666666699999f11111111bbcf666669999f111111111bccf99966666666f1111111111111bbcf666999999fffffff1bf1ff1f11ffff11f11ff6666fbf1bbfccfcffb
                f66666666999f1111111111bccff666666699999f11111111bbcf66666999ff111111111bcff9996666666ff1111111111111bccf6669999999999fff1f1ffbffffcf1ffff111ff666ff11bffcccffbb
                f66666666999f1111111111bccf6666666999999f11111111bccf66666999ff111111111bcf99996666666ff1111111111111bccf6699999999999ffffffbf1fff1bcfffff1111ff66f11bbfcfffbbbb
                f66666666999f111111111bbccf666666699999f11111111bbccf66669999f1111111111bcf99996666666ff1111111111111bcf66999999999999ff1fbf1ffff11bcfffff1111ff66f1bbfcfbbbbbbc
                f66666666999f111111111bbccf666666699999f11111111bbccf66669999f1111111111bcf99996666666ff1111111111111bcf66999999999999ffff1f1f11111bbcffffbb11ff66ffffffbbbb1bcc
                666666669999f111111111bbccf666666699999f11111111bbcff66669999f1111111111bcf99999666666ff1111111111111bcf66999999999999ff1f1ff1111111bcfffffffbfff666ff6fbb111ccc
                666666699999f111111111bbccf666666699999f11111111bbcf666699999f111111111bbcf99999666666ff1111111111111bcf66999999999999ff1fff11111111bcffff11fb1fff66666fb111ccfc
                666666999999f111111111bbccf666666999999f11111111bbcf666699999f111111111bccf99999666666f11111111111111bcf66999999999999f1ff1111111111bcff11b111111f66666f111cffcc
                666666999999f111111111bbccf666666999999f1111111bbbff66669999ff111111111bcff99999966666f11111111111111bcf66999999999999f111111111111bbfff1bb111111ff6666f11cfcccc
                666669999999f111111111bbccf66666699999f11111111bbcf666669999ff111111111bcff9999996666ff1111111111111bbcf66999999999999f111111111111bcffbf1111b111fff666ffccfcccb
                66669999999ff111111111bccff66666699999f11111111bbcf666669999ff111111111bcf99999996666ff1111111111111bccf66999999999999f111111111111bff11b1111bbb11bf6666ffffffbb
                66669999999f1111111111bccff66666699999f11111111bbcf666669999f1111111111bcf99999996666ff111111111111bbcff66999999999999f111111111111fffff11111bb11bbf66666fffbb1b
                66699999999f1111111111bccff66666699999f11111111bbcf666669999f1111111111bcf99999996666ff111111111111bcfff66999999999999f11111111111fff11b11111b11ffff66666666f11b
                66699999999f111111111bbccf666666699999f11111111bbcf666669999f111111111bbcf99999996666ff111111111111bcfff66699999999999f11111111111fffff11111b1ffff6666666666ff11
                66699999999f111111111bccff666666699999f11111111bbcf66666999ff111111111bbcf99999996666f1111111111111bcff666699999999999f1111111111fff1bf111111ff999666666666666ff
                66699999999f111111111bccff66666669999f111111111bbcf66666999f1111111111bbcf99999996666f1111111111111bcff666699999999999f111111111fff1bf111111f9999966666666666666
                66999999999f111111111bccf666666669999f111111111bccf66666999f1111111111bccf9999999666ff111111111111bbcff666699999999999f111111111ffffff11111bf9999966666666666666
                66999999999f111111111bccf666666669999f111111111bccf66666999f1111111111bccf9999999666ff111111111111bccff666699999999999f11111111fff1bff11111bf9999966666666666666
                6699999999ff111111111bcff666666669999f111111111bccf6666699f11111111111bccf9999999666ff111111111111bccff666669999999999f11111111f1ffff111111ff9999966666666666666
                6699999999ff111111111bcff666666669999f111111111bccf6666999f11111111111bccf9999996666f1111111111111bccff666669999999999f1111111f1111bf111111f99999966666666666666
                6699999999f1111111111bcff666666669999f11111111bbcff6666999f11111111111bccf9999996666f1111111111111bbcff666669999999999f111111ff1fffff111b11f99999966666666666666
                6699999999f1111111111bcff666666669999f11111111bbcff666699ff11111111111bcff999999666ff11111111111111bcff666669999999999f111111fff1bf1111b11f999999666666666666666
                6699999999f1111111111bcff66666666999f111111111bbcff666699ff11111111111bcff999996666ff11111111111111bcff666666999999999f11111111fffffccb111f999999666666666666666
                669999999ff1111111111bcff66666666999f111111111bbcff666699f111111111111bcf9999996666ff11111111111111bcff66666699999999f11111111111bffcbb11ff999999666666666666666
                669999999ff1111111111bcff66666666999f111111111bbcff666699f11111111111bbcf9999996666ff11111111111111bcff66666699999999f11111111111bfcfb11ff9999999666666666666666
                669999999f11111111111bcff66666666999f11111111bbbcf666669ff11111111111bcf99999966666f111111111111111bcff66666699999999f11111111111bfbb11fff9999999666666666666666
                669999999f11111111111bcff66666666999f11111111bbccf666669ff1111111111bbcf9999996666ff111111111111111bcff66666699999999f11111111111bfbb1f9999999999666666666666666
                66999999ff11111111111bcff66666666999f11111111bbccf666669f11111111111bcff9999966666ff111111111111111bcff6666669999999ff11111111111bffff99999999999666666666666666
                66999999ff11111111111bcff6666666699f111111111bbccf666669f11111111111bcff9999966666ff111111111111111bcff6666669999999f111111111111bbcf999999999999666666666666666
                66699999ff11111111111bcff666666669ff111111111bbcff666669f1111111111bbcf99999966666f111111111111111bbccf6666669999999f111111111111bcf9999999999996666666666666666
                66699999ff11111111111bcff666666669ff111111111bccff666669f1111111111bbcf99999966666f111111111111111bbccf6666666999999f111111111111bcf9999999999996666666666666666
                66699999ff1111111111bbcff666666669ff111111111bccf6666669f1111111111bbcf99999666666f111111111111111bbccf6666666999999f111111111111bcf9999999999996666666666666666
                66699999f11111111111bccff666666669ff111111111bccf6666669f1111111111bbcf99999666666f111111111111111bbccf6666666999999f111111111111bcf9999999999996666666666666666
                6669999ff1111111111bbccff666666669ff111111111bccf6666669f1111111111bbff99996666666f111111111111111bbbcf666666699999ff111111111111bcf9999999999996666666666666666
                6666699ff1111111111bbcfff666666669f1111111111bcff6666699f1111111111bcff99996666666f1111111111111111bbcf666666699999ff111111111111bcf9999999999966666666666666666
                6666699f11111111111bccfff666666669f1111111111bcff6666699f1111111111bcff99996666666f1111111111111111bbcf666666699999f1111111111111bcf9999999999966666666666666666
                666669ff11111111111bcffff666666669f1111111111bcff6666699f1111111111bcff99966666666f1111111111111111bbcf666666699999f1111111111111bcf999999999966666666666666666f
                666669f111111111111bcffff666666669f1111111111bcff6666699f1111111111bcff99966666666f1111111111111111bbcf666666699999f1111111111111bcf99999999996666666666666666ff
                666669f111111111111bcffff666666669f1111111111bcff6666699f1111111111bcff99966666666f1111111111111111bbcf66666669999ff1111111111111bcf99999999996666666666666666f1
                666669f11111111111bbcffff666666669f111111111bbcff666669ff1111111111bcff99966666666f1111111111111111bbcf66666669999f11111111111111bcf99999999996666666666666666f1
                66666ff11111111111bbcfff666666666ff111111111bccff666669ff1111111111bcff99966666666f1111111111111111bbcf66666669999f11111111111111bcf9999999999666666666666666ff1
                66666ff11111111111bbcfff666666666ff111111111bccff666669f11111111111bcff99966666666f1111111111111111bbcf66666669999f11111111111111bcf9999999996666666666666666f11
                66666f111111111111bbcfff666666666ff111111111bccff666669f11111111111bcff99966666666f1111111111111111bbcf6666666999ff11111111111111bcf9999999996666666666666666f11
                66666f111111111111bcffff666666666f111111111bbccff666669f11111111111bcff9996666666ff1111111111111111bbcf6666666999ff11111111111111bcf9999999996666666666666666f11
                6666ff111111111111bcffff66666666ff111111111bbcff6666669f11111111111bcff9996666666ff1111111111111111bbcf6666666999ff11111111111111bcf999999999666666666666666ff11
                666ff1111111111111bcffff66666666ff111111111bbcff6666669f11111111111bcff9966666666ff1111111111111111bbcf6666666999ff11111111111111bcff99999999666666666666666f111
                6fff11111111111111bccfff66666666f1111111111bbcff6666666f11111111111bcff9966666666ff1111111111111111bbcf6666666999ff1111111111111bbcff9999999966666666666666ff111
                ff1111111111111111bccfff6666666ff1111111111bccff6666666f11111111111bcff9966666666ff1111111111111111bbcf6666666999ff1111111111111bbccf9999999966666666666666f1111
                f11111111111111111bccfff6666666ff1111111111bccff6666666f11111111111bcff9966666666ff1111111111111111bbcf666666669fff1111111111111bbccf9999999666666666666666f1111
                111111111111111111bccfff6666666ff1111111111bccff6666666f11111111111bcff9666666666ff1111111111111111bbcf666666666ff11111111111111bbccff99999966666666666666ff1111
                111111111111111111bccfff666666fff1111111111bcccff666666f11111111111bcff9666666666ff1111111111111111bbcf666666666ff111111111111111bbcff99999966666666666666ff1111
                111111111111111111bcccff666666ff11111111111bbccfff66666f11111111111bcff6666666666ff1111111111111111bbcf666666666ff111111111111111bbccf9999996666666666666f111111
                111111111111111111bcccfff66666ff11111111111bbccfff6666ff11111111111bcff6666666666ff1111111111111111bbcff66666666ff111111111111111bbbcf9999966666666666666f111111
                111111111111111111bcccfff6666ff111111111111bbcccff6666ff11111111111bcff6666666666ff1111111111111111bbcff66666666ff111111111111111bbbcf9999966666666666666f111111
                111111111111111111bcccffff666ff111111111111bbcccff6666ff11111111111bcff666666666ff11111111111111111bbcfff6666666ff111111111111111bbbcff99996666666666666f1111111
                111111111111111111bccccffffffff111111111111bbcccfff666ff11111111111bccf66666666fff1111111111111111bbbcfff6666666ff111111111111111bbbcfff996666666666666f11111111
                f11111111111111111bccccfffffff1111111111111bbcccffff66ff11111111111bccfff666666fff1111111111111111bbbcffff66666fff111111111111111bbbccfff96666666666666f11111111
                f1111111111111111bbcccccffffff1111111111111bbccccfffffff11111111111bccffff66ffffff1111111111111111bbbcfffff6666fff11111111111111bbbbccffff666666666666ff11111111
                ff111111111111111bbcccccffffff1111111111111bbccccffffff11111111111bbcccffffffffff11111111111111111bbbccfffff66ffff11111111111111bbbbcccffffff66666666ff111111111
                ff111111111111111bccccccfffff11111111111111bbbcccffffff11111111111bbbccfffffffff11111111111111111bbbcccffffffffff111111111111111bbbcccccffffffffffffff1111111111
                ff1111111111111bbbccccccfffff1111111111111bbbbccccfffff11111111111bbbbccffffffff1111111111111111bbbbccccffffffff1111111111111111bbbccccccfffffffffffff111111111b
                fff111111111111bbccccccccffff1111111111111bbbbcccccfff11111111111bbbbbccffffffff1111111111111111bbbcccccfffffff111111111111111bbbbbccccccffffffffffff111111111bb
                ffff1111111111bbbccccccccffff1111111111111bbbbcccccfff11111111111bbbbccccffffff1111111111111111bbbbccccccfffff1111111111111111bbbbccccccffffffffffff111111111bbb
                ffff111111111bbbcccccccccffff111111111111bbbbbcccccfff1111111111bbbbbcccccfffff111111111111111bbbbccccccccfff1111111111111111bbbbbccccccfffffffffff111111111bbbb
                fffffb1111111bbbcccccccffffffff11111111bbbbbbbccccffff111111111bbbbbbcccccfffff11111111111111bbbbbcccccccfffffb1111111111111bbbbbcccccfffffffffffff11111111bbbbb
                fffffbb11111bbbbccccffffffffffff11111bbbbbbbbccccfffffbb1111bbbbbbbbcccccfffffff111111111111bbbbbccccccfffffffbb11111111111bbbbbbcccccffffffffffffff11111bbbbbbb
                ffffffbbbbbbbbbbccfffffffffffffff111bbbbbbbbccccfffffffbbbbbbbbbbbbccccccffffffff1111111111bbbbbccccccfffffffffbbbbbbbbbbbbbbbbbccccfffffffffffffffffbbbbbbbbbbc
                ffffffbbbbbbbbbccffffffffffffffffff1bbbbbbbcccccffffffffbbbbbbbbcccccccfffffffffffbb11111bbbbbbcccccffffffffffffbbbbbbbbbbbbbbbccccfffffffffffffffffffbbbbbbcccc
                ffffffffbbbbbbcfffffffffffffffffffffffcccccccffffffffffffbbbbbbbccccccffffffffffffffbbbbbbbbcccccccffffffffffffffffbbbbbbbbbbcccffffffffffffffffffffffffbccccccc
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbbbbcccccffffffffffffffffffffffcccccfffffffffffffffffffffffffbbbfffffffffffffffffffffffffffffffcccccc
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccc
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    """))
    ms4 = sprites.create(img("""
            ................................................
                    ................................................
                    ..................................fff...........
                    ..................................f11ff.........
                    .........ff......................f111ff.........
                    .......fffff..................ffff1f1ff.........
                    ......ff1f1ffff..............ff1f1bf1fff........
                    .....ff111ffffff.............f11f1bfff1f........
                    .....f11f11ff11ff............f1cf1bc111f........
                    .....f1bf11ff111f.........ffff1cff1c111f........
                    .....f1bfffffb11fff.....fff11f1ffff1b1f.........
                    ....ff11cf..ff1ffffff...f11fff1f...f11f.........
                    ...ff1ff1f..f111f111ffffffff1fcf...f11f.........
                    ...f11f1f...fff1fcfff11ffcc11fff...f11f.........
                    ..f11f11f....ffbcff11111fffc1ff...ff11f.........
                    .f1ffff1f.....fccf11111111fcfff..ff111ff........
                    .fbf..fbf.....fcf1111ffb11fffff.f1111111ff......
                    .fff..ff......fff111fffb11ffcff.f1fc1f1f1ff.....
                    .ff..ff......ffff111fbb1fffc1ff.ff.f1fb1f1f.....
                    ..ff.......fff1ff111fff1fcf1fffff..fbffbfff.....
                    ..........ff1111ffffffffcbfffffff..ffffff.f.....
                    ..........f11fffffcccf1fcbff11f1ff..ff.ff.......
                    .........fffff1cfffff1fcb1f111fc1f...f..f.......
                    .......fff1f11cfff111ffc11fc11fffff.............
                    .......f1fff1cffcffffccb11ffcff1ff1f............
                    .......ff11fffffbcfffbb111ffffc11fffff..........
                    ......ff1111ff.f1bfefb11ffe22ffc11f11ff.........
                    .....ffffcff....fffffffff4222ffffff111ff........
                    ....fff1fff.....f2feeffe42224f..ff11111f........
                    ...ff1ff.......ff2ffeef42224ff...fcf111f........
                    ..ff1fff.....ffff24ffff4224ff....ffff11f........
                    .ff1ff1f....ff1ff44ffe4444fff......ff11f........
                    .f1f.fcf...ffb1fffefeeeeeffbf....ffff111f.......
                    .fbf.ff....fbb1fffffffeffb1bff..ff111111ff......
                    .ff...f....fb11ff1cffff11111bf..f1fb1f1f11f.....
                    ..ff.f...ffbb111f1fff111bbbff1..fffff1f1fc1f....
                    .........fbb1111fffcc1ff11111f..ff..fbfbffff....
                    ........ffbf1111fffffff1b111bf...f..fffff.ff....
                    .......ffbbf111fff..ff111b1b1ff.....ff.ff.f.....
                    .......f1f1f111fcff..f111bb111f......f.ff.......
                    .......f1fff11ffcff..f1111b111f.....ff.f........
                    .......fffffffffcff..fff1ffffff.................
                    .......ffcf....f1f.....fff111f..................
                    ........fff...ff1f.....ffc1fff..................
                    ............fff11f....f1ffff....................
                    ...........ffcf11f....f1f1ff....................
                    ...........ffffff.....fcff1ff...................
                    ......................ffccfccf..................
        """),
        SpriteKind.E3)
    ms4.set_position(119, 67)
    p1.destroy()
    pause(1000)
    game.show_long_text("...", DialogLayout.BOTTOM)
    p1 = sprites.create(img("""
            ................................................
                    ...................fffffffffff..................
                    ..................fbbbbbbbbbbff.................
                    ..................fbbbcbccbcbbf.................
                    .................ffbbbbbbbbbffffffff............
                    .................fbbbbbbbcffbbbbbbbffff.........
                    .................fcbbbbbcfbbccccccccbbf.........
                    .................fccccccfbcccccccccccff.........
                    ..............ff6ffffffffffffffffffff...........
                    .............ff9ffefbbbffffbbfffff..............
                    .............f49fefdddd1ffddd1ffdf..............
                    .............f49ffffddd1ffddd1ffdf..............
                    .............f4496ffdddd33ddddd3ff..............
                    .............f44eefffdddddfddfddf...............
                    ........ff.ff44eeeefffddddfffddff...............
                    ........ffff44eeeeeeffffddddbfff................
                    .........ffffeeeeeeffffffddbf...................
                    ............ffeefffffff6ffdbffffff..............
                    .............ffffff44f966ffff6ff44ff............
                    ...............ffff455f6999ff669f4fff...........
                    ..............ff999f555f699fff966ff9f...........
                    ............ff999999f55f66669ff969fff...........
                    ...........ff9999966f44f9669999f999fff..........
                    ..........f999966666f44f99999f9f999f6ff.........
                    ..........f9996666fff44f9999999f966f99ff........
                    ..........f99966ffeffef999999f9f66ff6999f.......
                    ..........f9996ffeeeff669996669f6f.ff699f.......
                    ..........f99999fffefff666666fffff..ff699f......
                    ..........ff666999fefffffffffffccf.ff6999ff.....
                    ...........ff66669ffffffccccccccbf.f666999f.....
                    ............ff66fffdffccccccccccbfff66699ff.....
                    .............ffffdddfffccccccccbbfff6699ff......
                    ...............fddddffccccccccbbbffd669ff.......
                    ............ffffdddbffffffffffffffbdffff........
                    ............fdddddbfcfccbbbbbbbfffbddf..........
                    ............ffbbbbffcbcbbbbbbbbbbbfbddf.........
                    .............ffffffcbccbbbbbbbbbbbffbbf.........
                    ..............fffffcbcbbbbbbbbbbbbbffff.........
                    ................fccbccbbbbbbbbbbbbbfff..........
                    ................fcccccbbbbbbbbbbbbbbbf..........
                    ................fcccbbbbbbbffffbbbbbbbf.........
                    ................fccbbbbbbbbfffcbbbbbbbbf........
                    ................fccbbbbbbbbffccbbbbbbbbff.......
                    ................fcbbbbbbbbbfffccbbbbbbbbf.......
                    ................fbbbbbbbbbbf.ffcbbbbbbbbf.......
                    ................fbbbbbbbbbff..fccbbbbbbbbf......
                    ...............ffbbbbbbbbff...ffccbbbbbbbf......
                    ...............fbbbbbbbbff.....ffcbbbbbbbbf.....
        """),
        SpriteKind.player)
    p1.set_position(16, 64)
    game.show_long_text("茉莉:又被順移了", DialogLayout.BOTTOM)
    game.show_long_text("這次又是...甚麼呢?", DialogLayout.BOTTOM)
    game.show_long_text("通過香蕉狗問題的茉莉", DialogLayout.BOTTOM)
    game.show_long_text("正前往氣場沉重的鈣王領地", DialogLayout.BOTTOM)
    game.show_long_text("茉莉:這裡的氣場好沉重", DialogLayout.BOTTOM)
    game.show_long_text("鈣王：你是...人類！？", DialogLayout.BOTTOM)
    game.show_long_text("茉莉:原來如此！", DialogLayout.BOTTOM)
    game.show_long_text("難怪打球會爛", DialogLayout.BOTTOM)
    game.show_long_text("是因為4隻手會纏在一起吧", DialogLayout.BOTTOM)
    game.show_long_text("鈣王：是香蕉狗告訴你的？", DialogLayout.BOTTOM)
    game.show_long_text("嗐...那傢伙", DialogLayout.BOTTOM)
    game.show_long_text("老是愛跟別人裝熟", DialogLayout.BOTTOM)
    game.show_long_text("勸你離題遠點", DialogLayout.BOTTOM)
    game.show_long_text("他個性其實很糟糕", DialogLayout.BOTTOM)
    game.show_long_text("茉莉:我是來取得碎片的", DialogLayout.BOTTOM)
    game.show_long_text("鈣王：好久沒遇到人類了", DialogLayout.BOTTOM)
    game.show_long_text("來比試一下贏了就給你", DialogLayout.BOTTOM)
    p1.destroy()
    p1 = sprites.create(img("""
            ................................................
                    ...................fffffffffff..................
                    ..................fbbbbbbbbbbff.................
                    ..................fbbbcbccbcbbf.................
                    .................ffbbbbbbbbbffffffff............
                    .................fbbbbbbbcffbbbbbbbffff...f.....
                    .................fcbbbbbcfbbccccccccbbf...ff....
                    .................fccccccfbcccccccccccff..f1ff...
                    ..............ff6ffffffffffffffffffff....f11f...
                    .............ff9ffefbbbffffbbfffff......ff15f...
                    .............f49fefdddd1ffddd1ffdf......f15ff...
                    .............f49ffffddd1ffddd1ffdf......f15f....
                    .............f4496ffdddd33ddddd3ff.....ff15f....
                    .............f44eefffdddddfffdddf......f15ff....
                    ........ff.ff44eeeefffddddffdddff.....ff15f.....
                    ........ffff44eeeeeeffffddddbfff......f155f.....
                    .........ffffeeeeeeffffffddbf.........f155f.....
                    ............ffeefffffff6ffdbffffff...ff55ff.....
                    .............ffffff44f966ffff6ff44ff.f155f......
                    ................fff455f6999ff669f4ffff15ff......
                    ...............ff99f555f699fff966ff9ff55f.......
                    ...............f9999f55f66669ff969fff15ff.......
                    ...............f9999f44f9669999f999ff55f........
                    ...............f9999ff4f99999f9f999f15ff........
                    ...............ff9996fff9999999f96ff15f.........
                    ................f699996f99999f9f6fff5ff.........
                    ................ff999996f996669f6f155f..........
                    .................f6999999f666fff9f155f..........
                    .................ff699996ffff999f155ff..........
                    ..................ff6996999ff999f155ff..........
                    ...................ff6999999f99ff15f6f..........
                    ....................fff99999ffff155f6f..........
                    ...................fffff999ffffff5ff6f..........
                    ...................ffccff9ffddfffff6f...........
                    ...................fccccfffddddfffff............
                    ..................ffcbccffdddddddfbf............
                    ..................fcbccbffddddddffbf............
                    .................ffcbcbbbffbddbffbbf............
                    ................fccbccbbbbffbbffbbbbff..........
                    ................fcccccbbbbbfffbbbbbbbf..........
                    ................fcccbbbbbbbfffbbbbbbbbf.........
                    ................fccbbbbbbbbffcbbbbbbbbbf........
                    ................fccbbbbbbbbffccbbbbbbbbff.......
                    ...............ffcbbbbbbbbbfffccbbbbbbbbf.......
                    ...............ffbbbbbbbbbbf.ffcbbbbbbbbf.......
                    ..............fffbbbbbbbbbff..fccbbbbbbbbf......
                    ..............fffbbbbbbbbff...ffccbbbbbbbf......
                    ..............ffbbbbbbbbff.....ffcbbbbbbbbf.....
        """),
        SpriteKind.player)
    p1.set_position(16, 64)
    game.splash("請選擇攻擊武器")
    mySprite.say(game.ask("a雷電鐵絲 b木槌"))
    if controller.A.is_pressed():
        game.show_long_text("茉莉使用螢光劍", DialogLayout.BOTTOM)
        game.show_long_text("鈣王空手打斷螢光劍", DialogLayout.BOTTOM)
        game.show_long_text("鈣王使用赤手空拳", DialogLayout.BOTTOM)
        game.show_long_text("茉莉受傷", DialogLayout.BOTTOM)
        game.show_long_text("茉莉使用帽子", DialogLayout.BOTTOM)
        game.show_long_text("鈣王迴避", DialogLayout.BOTTOM)
        game.show_long_text("茉莉受傷", DialogLayout.BOTTOM)
        game.show_long_text("鈣王使用大招", DialogLayout.BOTTOM)
        game.show_long_text("(五馬分屍)", DialogLayout.BOTTOM)
        game.show_long_text("茉莉使用香蕉皮", DialogLayout.BOTTOM)
        game.show_long_text("鈣王滑倒", DialogLayout.BOTTOM)
        game.show_long_text("鈣王再次使用大招", DialogLayout.BOTTOM)
        game.show_long_text("茉莉使用雷電鐵絲", DialogLayout.BOTTOM)
        game.show_long_text("綁住鈣王並電擊", DialogLayout.BOTTOM)
        game.show_long_text("鈣王電倒", DialogLayout.BOTTOM)
        game.show_long_text("鈣王：啊...你....", DialogLayout.BOTTOM)
        game.show_long_text("碎片...", DialogLayout.BOTTOM)
        game.show_long_text("給你吧...", DialogLayout.BOTTOM)
        game.show_long_text("(昏倒)", DialogLayout.BOTTOM)
        game.show_long_text("茉莉：終於...", DialogLayout.BOTTOM)
        game.show_long_text("鑰匙總算湊齊了", DialogLayout.BOTTOM)
        game.show_long_text("（遺跡碎片*1）", DialogLayout.BOTTOM)
        ms4.destroy()
    else:
        game.show_long_text("四手:別忘了", DialogLayout.BOTTOM)
        game.show_long_text("我可是骨頭呢", DialogLayout.BOTTOM)
        game.show_long_text("根本沒傷害", DialogLayout.BOTTOM)
        game.show_long_text("你已死亡", DialogLayout.BOTTOM)
        game.show_long_text("請重新遊玩", DialogLayout.BOTTOM)
        game.reset()
sprites.on_destroyed(SpriteKind.E2, on_on_destroyed2)

def on_on_destroyed3(sprite):
    global mySprite3, p1
    scene.set_background_image(img("""
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                eee4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444eee
                eee4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444eee
                eee4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444eee
                eee4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444eee
                eee4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444eee
                eee4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444eee
                eee4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444eee
                eee4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444eee
                eee444444eeeeeeeeeeeeeeeeeeeeeeeeee44444444444444eeeeeeeeeeeeeeeeeeeeeeeeeee444444444444444444eeeeeeeeeeeeeeeeeeeeeeee444444444444eeeeeeeeeeeeeeeeeeeeeee4444eee
                eee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeee4444444444444eeeeeeeeeeeeeeeeeeeeeeeeeee444444444444444444eeeeeeeeeeeeeeeeeeeeeeee44444444444eeeeeeeeeeeeeeeeeeeeeeee4444eee
                eee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeee444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeee4444444444444444eeeeeeeeeeeeeeeeeeeeeeeeeee444444444eeeeeeeeeeeeeeeeeeeeeeeee444eee
                eee4444eeeeeee6666666666666666eeeeee444444444444eeeeeee6666666666666666eeeeee444444444444444eeeeee66666666666666666eeeee44444444eeeeeeeeeeeeeeeeeeeeeeeeee444eee
                eee4444eeeeeee6666666666666666eeeeee444444444444eeeeeee6666666666666666eeeeee444444444444444eeeeee66666666666666666eeeee44444444eeeeeee66666666666666eeeee444eee
                eee4444eeeeeee6666666666666666eeeeee444444444444eeeeeee6666666666666666666eee444444444444444eeeeee66666666666666666eeeee44444444eeeeeee66666666666666eeeee444eee
                eee4444eee66666666666666666666666eee444444444444eee66666666666666666666666eee444444444444444eee6666666666666666666666eee44444444eeee6666666666666666666eee444eee
                eee4444eee66666666666666666666666eee444444444444eee66666666666666666666666eee444444444444444eee6666666666666666666666eee44444444eeee6666666666666666666eee444eee
                eee4444eee66666666666666666666666eee444444444444eee66666666666666666666666eee444444444444444eee6666666666666666666666eee44444444eeee6666666666666666666eee444eee
                eee4444eee66666666666666666666666eee444444444444eee66666666666666666666666eee444444444444444eee6666666666666666666666eee44444444eeee6666666666666666666eee444eee
                eee4444eee66666666666666666666666eee444444444444eee66666666666666666666666eee444444444444444eee6666666666666666666666eee44444444eeee6666666666666666666eee444eee
                eee4444eee66666666666666666666666eee444444444444eee66666666666666666666666eee444444444444444eee6666666666666666666666eee44444444eeee6666666666666666666eee444eee
                eee4444eee66699999999999999999666eee444444444444eee66699999999999999999666eee444444444444444eee6666666666666666666666eee44444444eeee6666666666666666666eee444eee
                eee4444eee66699999999999999999666eee444444444444eee66699999999999999999666eee444444444444444eee6669999999999999999666eee44444444eeee6666666666666666666eee444eee
                eee4444eee66699999999999999999666eee444444444444eee66699999999999999999666eee44eee4444444444eee6669999999999999999666eee44444444eeee6669999999999999666eee444eee
                eee4444eee99999999999999999999999eee444444444444eee99999999999999999999999eee44eeee444444444eee6669999999999999999666eee44444444eeee6669999999999999666eee444eee
                eee4444eee99999999999999999999999eee444444444444eee99999999999999999999999eeeee55eee44444444eee9999999999999999999999eee44444444eeee6669999999999999666eee444eee
                eee4444eee99999999999999999999999eee444444444444eee99999999999999999999999eeee555e5ee4444444eee9999999999999999999999eee44444444eeee9999999999999999999eee444eee
                eee4444eee99999999999999999999999eee444444444444eee99999999999999999999999eeee5555eeee444444eee9999999999999999999999eee44444444eeee9999999999999999999eee444eee
                eee4444eee99999999999999999999999eee444444444444eee99999999999999999999999eeee555555eee44444eee9999999999999999999999eee44444444eeee9999999999999999999eee444eee
                eee4444eee99999999999999999999999eee444444444444eee99999999999999999999999eeee5555555eeee444eee9999999999999999999999eee44444444eeee9999999999999999999eee444eee
                eee4444eee99999999999999999999999eee444444444444eee99999999999999999999999eeee555555555eee44eee9999999999999999999999eee44444444eeee9999999999999999999eee444eee
                eee4444eee99999999999999999999999eee444444444444eee99999999999999999999999eeee5555555555ee44eee9999999999999999999999eee44444444eeee9999999999999999999eee444eee
                eee4444eee99999999999999999999999eee444444444444eee99999999999999999999999eeee555555555555e4eee9999999999999999999999eee44444444eeee9999999999999999999eee444eee
                eee4444eee99999999999999999999999eee444444444444eee999999999999999999999eeeeeee55555555555eeeee9999999999999999999999eee44444444eeee9999999999999999999eee444eee
                eee4444eee99999999999999999999999eee444444444444eee999999999999999999999eeeeeee55555555555eeeee9999999999999999999999eee44444444eeee9999999999999999999eee444eee
                eee4444eee99999999999999999999999eee444444444444eee999999999999999999999eeeeeeeeee555555555eeee9999999999999999999999eee44444444eeeeee999999999999999eeeee444eee
                eee4444eeeeeee9999999999999999eeeeee444444444444eeeeee9999999999999999eeeeeeeeeeee555555555eeeeeee9999999999999999eeeeee44444444eeeeee999999999999999eeeee444eee
                eee4444eeeeeee9999999999999999eeeeee444444444444eeeeee9999999999999999eeeeeeeeeeeee555555555eeeeee9999999999999999eeeeee44444444eeeeee999999999999999eeeee444eee
                eee4444eeeeeee9999999999999999eeeeee444444444444eeeeee9999999999999999eeeeeeeeeeeee555555555eeeeee9999999999999999eeeeee44444444eeeeeeeeeeeeeeeeeeeeeeee44444eee
                eee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeee444444444444eeeeeeeeeeeeeeeeeeeeeee55555e5eeeeeee55555555eeeeeeeeeeeeeeeeeeeeeeeeeee44444444eeeeeeeeeeeeeeeeeeeeeeee44444eee
                eee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeee444444444444eeeeeeeeeeeeeeeeeeeeee55555555eeeeeeee55555eeeeeeeeeeeeeeeeeeeeeeeeeee44444444444eeeeeeeeeeeeeeeeeeeeeee44444eee
                eee444444eeeeeeeeeeeeeeeeeeeeeeeee44444444444444444eeeeeeeeeeeeeee55555555555eeeeeeeee5555555eeeeeeeeeeeeeeeeeeeeeeeee444444444444444444444444444444444444444eee
                eee4444444444444444444444444444444444444444444444444444444ee55555555555555555eeeeeeeee5555555eeeeee4444444444444444444444444444444444444444444444444444444444eee
                eee44444444444444444444444444444444444444444444444444444ee555555555555555555eeeeeeeeeee5555ffffeee44444444444444444444444444444444444444444444444444444444444eee
                eee44444444444444444444444444444444444444444444444444444e555555555555555555eeeeeeeeeeee55555fffffe44444444444444444444444444444444444444444444444444444444444eee
                eee444444444444444444444444444444444444444444444444444eee555555555555555555eeeeeeeeeeee555555ffffe44444444444444444444444444444444444444444444444444444444444eee
                eee444444444444444444444444444444444444444444444444eee55555555555555555555eeeeeeeeeeeeee55555ffffe44444444444444444444444444444444444444444444444444444444444eee
                eee444444444444444444444444444444444444444444444eeee55555555555555555555eeeeeeeeeeeee55eee555fffe444444444444444444444444444444444444444444444444444444444444eee
                eee44444444444444444444444444444444444444444444eee55555555555555555555eeeeeeeeeeeeee55eeeeeefffee444444444444444444444444444444444444444444444444444444444444eee
                eee444444444444444444444444444444444444444444ee555555555555555555555eeeeeeeeeeeeeeee55eeeeeefffe4444444444444444444444444444444444444444444444444444444444444eee
                eee444444444444444444444444444444444444444eee555555555555555555555eeeeeee444eeeeeee555555eeeeee44444444444444444444444444444444444444444444444444444444444444eee
                eee44444444444444444444444444444444444eeee5555555555555555555555ee5ee5554444eeeee555555555ee44444444444444444444444444444444444444444444444444444444444444444eee
                eee444444444444444444444444444444444ee555555555555555555555555555ee555554444eeeee555555555ee44444444444444444444444444444444444444444444444444444444444444444eee
                eee4444444444444444444444444444444ee5555555555555555555555555555e55555544444eeee5555e55555ee44444444444444444444444444444444444444444444444444444444444444444eee
                eee44444444444444444444444444444eee55555555555555555555555555555555555544444eeee5555e555555ee4444444444444444444444444444444444444444444444444444444444444444eee
                eee444444444444444444444444444ee45555555555555555555555555555555555555544444eee55555e555555ee4444444444444444444444444444444444444444444444444444444444444444eee
                eee4444444444444444444444444eee5555555555555555555555555e5555555555555444444ee55555e5555555ee4444444444444444444444444444444444444444444444444444444444444444eee
                eee444444eeeeee44444444444eee5555555555555555555555555555555555555555444444ee555555e5555555ee4444444444444444444444444444444444444444444444444444444444444444eee
                eee44ffffffffeeee44444eeee555555555555555555555555555e5555555555555554444eee555555ee5555555ee4444444444444444444444444444444444444444444444444444444444444444eee
                5ee4ffffffffffeeeeeeeeee555555555555555555555555555ee5555555555555544444eeee55555ee55555555ee4444444444444444444444444444444444444444444444444444444444444444eee
                eeeeffffffffffee555555555555555555555555555555555ee555555555555555444444eee555555e555555555ee4444444444444444444444444444444444444444444444444444444444444444eee
                5eeffffffffffff55555555555555555555555555555555ee5555555555555554444444ee5555555ee555555555ee4444444444444444444444444444444444444444444444444444444444444444eee
                e5eeffffffffffff555555555555555555555555555eeee55555555555555555444444e5e555555ee5555555555eee444444444444444444444444444444444444444444444444444444444444444eee
                5eefffffffffffffe555555555555555555555eeeee5555555555555555555444444eeee5555555e555555555554ee444444444444444444444444444444444444444444444444444444444444444eee
                555fffffffffffffeeeeee55555555eeeeeeee55555555555555555555555444444eee55555555ee5555555555544e444444444444444444444444444444444444444444444444444444444444444eee
                55555ffffffffffeeeeee555555555555555555555555555555555555544444444ee5555555555ee5555555555444e444444444444444444444444444444444444444444444444444444444444444eee
                555555efeeeeeeeee4ee555555555555555555555555555555555555444444444e555555555555ee5555555555444e444444444444444444444444444444444444444444444444444444444444444eee
                5555555eeeeeee44444e5555555555555555555555555555555544444444444e55555555555555e5555555555544ee444444444444444444444444444444444444444444444444444444444444444eee
                55555555e55eeeee444445555555555544455555555555555554444444444e555555555555555ee5555555555544ee444444444444444444444444444444444444444444444444444444444444444eee
                55555555555555eeee444444444444444444455555555555555444444444e5555555555555555e55555555555444ee444444444444444444444444444444444444444444444444444444444444444eee
                55555555555555555eee44444444444444444444444444444444444444455555555555555555ee555555555544444e444444444444444444444444444444444444444444444444444444444444444eee
                55555555555555555555eeee444444444444444444444444444444444e55555555555555555ee5555555555544444e444444444444444444444444444444444444444444444444444444444444444eee
                5555555555555555555555eeeee4444444444444444444444444444ee555555555555555555ee5555555555444444e444444444444444444444444444444444444444444444444444444444444444eee
                55555555555555555555555eeeeeeeeeeeee444444444444444eeee55555555555555555555e55555555555444444e444444444444444444444444444444444444444444444444444444444444444eee
                55555555555555555555555555544444444eeeeeeeeeeeeeeeeeee55555555555555555555ee5555555555544444ee444444444444444444444444444444444444444444444444444444444444444eee
                55555555555555555555555555555544444444eeeeeeeeeeeeee555555555555555555555e5e5555555555444444ee444444444444444444444444444444444444444444444444444444444444444eee
                55555555555555555555555555555555444444444444eeeeee5555555555555555555555ee55555555555544444ee4444444444444444444444444444444444444444444444444444444444444444eee
                5e5555555555555555555555555555555544444444444eee5555555555555555555e55eee555555555554444444e44444444444444444444444444444444444444444444444444444444444444444eee
                55e555555555555555555555555555555554444444444eee55555555555555555555555e555555555554444444ee44444444444444444444444444444444444444444444444444444444444444444eee
                555e555555555555555555555555555555554444444eeee55555555555555555555eeee555555555544444444eee44444444444444444444444444444444444444444444444444444444444444444eee
                5555ee5555555555555555555555555555555444444eeee55555555555555555555555555555555444444444eeeeee444eeeeeee44444444444444444444444444444444444444444444444444444eee
                555555eeee5555555555555555555555555554444eeee555555555555555555555555555555554444444444eeeeeeeeeeeeeeeeeeeeee444444444444444444444444444444444444444444444444eee
                5555555555eeeeeeeeeeeeeeee555eeeeee44444e55555555555555555555555555555555544444444444eeeeeeeeeeeeeeeeeeeeeeeeeeee44444444444444444444444444444444444444444444eee
                555555555555555555555eeeeeeeeeeeeeeee44ee555555555555555555555555555555544444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee444444444444444444444444444444444444444eee
                555555555555555555555555444444444444ee45555555555555555555ee55555555554444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444444444444444444444444444444444444eee
                55555555555555555555555555554444eeeeeee555555555555555eeee555555555544444444444eeeeeeeeeeeeeeeee555555555555eeeeeeeeeeeeeee4444444444444444444444444444444444eee
                55555555555555555555555555544eeeeee55555555555555eeeee55555555554444444444444eee555eeeee55555555555555555555555555eeeeeeeeee444444444444444444444444444444444eee
                55555555555555555555555555444eeeeeeeeeeeeeee5eeee55555555555444444444444444eeeeeeee5555555555555555555555555555555555eeeeeeee44444444444444444444444444444444eee
                5555555555555555555555555544e5eeee55555eeeeeee55555555555554444444444444eeeeeeeee55555555555555555555555555555555555555eeeeee44444444444444444444444444444444eee
                5555555555555555555555555444eee55555eeeee55555555555555554444444444444eeeeeee55555555555555555555555555555555555555555555eeeee4444444444444444444444444444444eee
                55555555555555555555555544eee555eeee555555555555555444444444444444eeeeeee555555555555555555555555555555555555555555555555555eee4fff44444444444444444444444444eee
                55555555555555555555555444ffffffeee5555555555555554444444444444eeeeeee55555555555555555555555555555555555555555555555555555555effff44444444444444444444444444eee
                555555555555555555555544fffffffffee555544455555544444444444444eeeeee5555555555555eeeeeeeeeee5555555555555555eeeeeeeeeeeeeeeee5fffffe4444444444444444444444444eee
                55555555555555555555544fffffffffffeeee544444444444444444444fffeee55555555555eeeee55555555555555555555555555555555555555555555ffffffffeeeeeeeeeeeeeeeeeeeeeeeeeee
                55555555555555555555544fffffffffffeeee54444444444444444eeeffeeeeeeee555555555555555555555555555555555555555555555555555555555ffffffffeeeeeeeeeeeeeeeeeeeeeeeeeee
                ee55555555555555555444efffffffffffeeeee444444444444444eeeeffffe44444555555555555555555555555555555555555555555555555555555555ffffffffeeeeeeeeeeeeeeeeeeeeeeeeeee
                ee55555555555555555eeeeeefffffffffeeeeeeeeeeeeeeeeeeeeeeeeffffe44444555555555555555555555555555555555555555555555555555555555fffffffeeeeeeeeeeeeeeeeeeeeeeeeeeee
                eee555555555eeeeeeeeeeeeeeffffffffe444444eeeeeeeeeeeee4444ffffe4444445555555555555555555555555555555555555555555555555555555fffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444444444444444eee44444ffffee444444555555555555555555555555555555555555555555555555555555fffffffee44444444444444444444eeeeeee
                4eeeeeeeee4444444444eeeeee44444444444444444444444444444444ffffeee44444455555555555555555555555555555555555555555555eeeeeeeeefffffffee444444444444444444444eeeeee
                444444eee4444444444444444444444444444444444444444444444444ffffeeeee4444444555555555555555555555555555555555555eeeeeeee44444eeeeeeeee44444444444444444444444eeeee
                44444444444444444444444444444444444444444444444444444444444444444eeee4444444455555555555555555555555555555eeeee4444444444444eeee444444444444444444444444eeeeeeee
                4444444444444444444444444444444444444444444444444444444444444444444444eee4444445555555555555555555555555ee444444444444444444444444444444444444444444eeeeeeeeeeee
                4444444444444444444444444444444444444444444444444444444444444444444444eeeeeeeeeeeee5555555555555eeeeeee44444444444444444444444444444444444444444444eeeeeeeeeeeee
                eeeeeeeee4444444444444444444444444444444444444444444444444444444444444444444eeeeeeee4eeeeeeeeeeee4444444444444444444444444444444444444444444444444eeeeeeee444444
                eeeeeeeeeeeee444444444444444444444444444444444444444444444444444444444444444444444444eeeeeeeeeeee4444444444444444444444444444444444444444444444444eeee4444444444
                5555eeeeeeeeeeeeeeeeeee4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444eeee444444445555
                455555555555555eeeeeeeeeeeeeeeeeeeeeeeeeeeee4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444eeeeee4444445555555
                455555555555555555555eeeeeeeeeeeeeeeeeeeeeeeeeeeee44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444eee444444555555555
                4555555555555555555555555555555555555555555eeeeeeeeeee44444444444444444444444444444444444444444444444444444444444444444444444444444444444444eeee4444455555555555
                45555555555555555555555555555555555555555555555eeeeeeeeeeeeeee4444444444444444444444444444444444444444444444444444444444444444444444444444eeee444444555555555555
                455555555555555555555555555555555555555555555555555555555eeeeeeeeeeee44444444444444444444444444444444444444444444444444444444444444444444eeee4444455555555555555
                45555555555555555555555555555555555555555555555555555555555eeeeeeeeeeeeeeee44444444444444444444444444444444444444444444444444444444444eeeeee44445555555555555554
                4555555555555555555555555555555555555555555555555555555555555555eeeeeeeeeeeeee444444444444444444444444444444444444444444444444444444eeeeee4444555555555555555544
                455ee44455555555555555555555555555555555555555555555555555555555555eee55555eee444444444444444444444444444444444444444444444444444eeeeeeee44445555555555555554444
                44555ee4445555555555555555555555555555555555555555555555555555555555555555555544444444444444444444444444444444444444444444444eeeeeeeeee44445555555555555555e4444
                4445555e4444555555555555555555555555555555555555555555555555555555555555555555ee44444444444444444444444444444444444444444eeeeeeeeeeee44455555555555555555ee44444
                444445555e44455555555555555555555555555555555555555555555555555555555555555555ee44444444444444444444444444444444444444444eeeeeee44444455555555555555555ee4444444
    """))
    mySprite3 = sprites.create(img("""
            ...........ffffffffffffffffffffff...............
                    ...........f9999999999999999f111ff..............
                    ..........f99ffffffff9999999f1111ff.............
                    ..........f9ffffff44f9999999ff11111ff...........
                    ..........f9fccff455ff9999999f111111f...........
                    ..........f9fffcf4555ff999999ff111111f..........
                    .........ff9fccfffffffff999996ff11111f..........
                    .........f999ff999996fef9999666f11111f..........
                    .........f9966f966666fef6666666f11111f..........
                    .........ffffffffffffffffffff66fdd111f..........
                    .........eeeeeeeeeeeee4444444fffffdd1f..........
                    .........ee55554e4555544555444444fffdff.........
                    ..........e5544e5ee4444555545555544fffff........
                    ..........eeeeeeeeeeee55555445555544e69ff.......
                    ..........ee5e11eeee5ee5555545555544ee699f......
                    .........ee154eeee1155545555455555444e6999f.....
                    .........e1155eeee1555544555455555444e6999f.....
                    .........e1555e444e455554555445555544e6999f.....
                    .........e5554e555ee4444e555545555544effff......
                    .........e55eeeeeee5eeeee555545555544e..........
                    .........eeee555455e45555555545555544e..........
                    ..........ee155455ee15555555545555544e..........
                    .........ee1555455e415555555545555544ee.........
                    .........e11544455e4554e55555455555444e.........
                    .........e55544555e4444e55555455555444e.........
                    .........e455e4555ee44e455555455555444e.........
                    .........e444e45555eeee45555545555544ee.........
                    ..........eee445555544445555545555544e..........
                    ...........e454555555ee45555545555544e..........
                    ..........eeeeee55555e555555545555544e..........
                    .........ee5555555555e555555545555444e..........
                    .........e1155555555e1155555545555444e..........
                    .........e155ee55555e1554ee5545555444e..........
                    .........e15ee455555e1554e45545555444e..........
                    .........e55e4455555e555ee4554555444ee..........
                    .........e55e4455555e555e45544555444e...........
                    .........eeee44555554eee455545554444e...........
                    ...........ee4555554455555545554444e............
                    ..........e444555554555554455544444e............
                    ..........e4445555445555545544444eee............
                    .........ee444555445555444444444ee..............
                    ........ee44455544555544444444eee...............
                    ........e4444454455544444444eee.................
                    ........f44444444444444eeeee....................
                    ........ffff4444444444ee........................
                    ........fcffff444444eee.........................
                    ........ffccff4eeeeee...........................
                    .........ffffff.................................
        """),
        SpriteKind.E2)
    mySprite3.set_position(133, 56)
    mySprite.destroy()
    p1.destroy()
    pause(1000)
    game.show_long_text("...", DialogLayout.BOTTOM)
    game.splash("終於有人類來了")
    game.show_long_text("香蕉狗(像香蕉的狗狗", DialogLayout.BOTTOM)
    game.show_long_text("無技能但喜歡猜謎)", DialogLayout.BOTTOM)
    p1 = sprites.create(img("""
            ................................................
                    ...................fffffffffff..................
                    ..................fbbbbbbbbbbff.................
                    ..................fbbbcbccbcbbf.................
                    .................ffbbbbbbbbbffffffff............
                    .................fbbbbbbbcffbbbbbbbffff.........
                    .................fcbbbbbcfbbccccccccbbf.........
                    .................fccccccfbcccccccccccff.........
                    ..............ff6ffffffffffffffffffff...........
                    .............ff9ffefbbbffffbbfffff..............
                    .............f49fefdddd1ffddd1ffdf..............
                    .............f49ffffddd1ffddd1ffdf..............
                    .............f4496ffdddd33ddddd3ff..............
                    .............f44eefffdddddfddfddf...............
                    ........ff.ff44eeeefffddddfffddff...............
                    ........ffff44eeeeeeffffddddbfff................
                    .........ffffeeeeeeffffffddbf...................
                    ............ffeefffffff6ffdbffffff..............
                    .............ffffff44f966ffff6ff44ff............
                    ...............ffff455f6999ff669f4fff...........
                    ..............ff999f555f699fff966ff9f...........
                    ............ff999999f55f66669ff969fff...........
                    ...........ff9999966f44f9669999f999fff..........
                    ..........f999966666f44f99999f9f999f6ff.........
                    ..........f9996666fff44f9999999f966f99ff........
                    ..........f99966ffeffef999999f9f66ff6999f.......
                    ..........f9996ffeeeff669996669f6f.ff699f.......
                    ..........f99999fffefff666666fffff..ff699f......
                    ..........ff666999fefffffffffffccf.ff6999ff.....
                    ...........ff66669ffffffccccccccbf.f666999f.....
                    ............ff66fffdffccccccccccbfff66699ff.....
                    .............ffffdddfffccccccccbbfff6699ff......
                    ...............fddddffccccccccbbbffd669ff.......
                    ............ffffdddbffffffffffffffbdffff........
                    ............fdddddbfcfccbbbbbbbfffbddf..........
                    ............ffbbbbffcbcbbbbbbbbbbbfbddf.........
                    .............ffffffcbccbbbbbbbbbbbffbbf.........
                    ..............fffffcbcbbbbbbbbbbbbbffff.........
                    ................fccbccbbbbbbbbbbbbbfff..........
                    ................fcccccbbbbbbbbbbbbbbbf..........
                    ................fcccbbbbbbbffffbbbbbbbf.........
                    ................fccbbbbbbbbfffcbbbbbbbbf........
                    ................fccbbbbbbbbffccbbbbbbbbff.......
                    ................fcbbbbbbbbbfffccbbbbbbbbf.......
                    ................fbbbbbbbbbbf.ffcbbbbbbbbf.......
                    ................fbbbbbbbbbff..fccbbbbbbbbf......
                    ...............ffbbbbbbbbff...ffccbbbbbbbf......
                    ...............fbbbbbbbbff.....ffcbbbbbbbbf.....
        """),
        SpriteKind.player)
    p1.set_position(16, 64)
    game.show_long_text("啊啊啊...", DialogLayout.BOTTOM)
    game.show_long_text("這又是哪裡了", DialogLayout.BOTTOM)
    game.show_long_text("打倒磷化氫的茉莉", DialogLayout.BOTTOM)
    game.show_long_text("被不明力量順移到", DialogLayout.BOTTOM)
    game.show_long_text("愛裝熟的香蕉狗地盤", DialogLayout.BOTTOM)
    game.show_long_text("茉莉:好多像香蕉的植物喔", DialogLayout.BOTTOM)
    game.show_long_text("香蕉狗：汪汪！嘿！兄弟～", DialogLayout.BOTTOM)
    game.show_long_text("歡迎來到第二關", DialogLayout.BOTTOM)
    game.show_long_text("茉莉：我跟你很熟嗎...", DialogLayout.BOTTOM)
    game.show_long_text("你是碎片的守衛吧", DialogLayout.BOTTOM)
    game.show_long_text("香蕉狗：哼哼", DialogLayout.BOTTOM)
    game.show_long_text("看來你直覺挺敏銳的", DialogLayout.BOTTOM)
    game.show_long_text("想要在我這裡拿到碎片", DialogLayout.BOTTOM)
    game.show_long_text("必須回答我一個問題！", DialogLayout.BOTTOM)
    game.show_long_text("茉莉：我都不知到要考試！", DialogLayout.BOTTOM)
    game.show_long_text("我又沒有念書！ ", DialogLayout.BOTTOM)
    game.show_long_text("香蕉狗：什麼東西有長有短", DialogLayout.BOTTOM)
    game.show_long_text("且有黃有綠", DialogLayout.BOTTOM)
    game.show_long_text("還能幫助你們人類瘦下來！", DialogLayout.BOTTOM)
    game.show_long_text("茉莉：呃…", DialogLayout.BOTTOM)
    game.show_long_text("香蕉....嗎？", DialogLayout.BOTTOM)
    game.show_long_text("香蕉狗：你..你怎麼知道", DialogLayout.BOTTOM)
    game.show_long_text("茉莉：呃...", DialogLayout.BOTTOM)
    game.show_long_text("（遺跡碎片*1）", DialogLayout.BOTTOM)
    game.show_long_text("香蕉狗：算了~", DialogLayout.BOTTOM)
    game.show_long_text("看你這麼聰明", DialogLayout.BOTTOM)
    game.show_long_text("偷偷告訴你一件事", DialogLayout.BOTTOM)
    game.show_long_text("你去的下一站的守護者", DialogLayout.BOTTOM)
    game.show_long_text("他打球超爛的", DialogLayout.BOTTOM)
    game.show_long_text("茉莉:欸不是！", DialogLayout.BOTTOM)
    game.show_long_text("告訴我這幹嘛！", DialogLayout.BOTTOM)
    game.show_long_text("而且外星人竟然會打球喔！", DialogLayout.BOTTOM)
    mySprite3.destroy()
sprites.on_destroyed(SpriteKind.E1, on_on_destroyed3)

mySprite2: Sprite = None
mySprite3: Sprite = None
ms4: Sprite = None
p1: Sprite = None
ms5: Sprite = None
K: Sprite = None
k3: Sprite = None
k2: Sprite = None
k1: Sprite = None
mySprite: Sprite = None
game.splash("尋找外星遺跡")
scene.set_background_image(img("""
    666676777777777777777777777777777777777777777777777777776777766666666666666667777777666666666677777777777777777777777777777777777777777777777777777777777777777c
        6666667777777777776677777777777777777777777777777777777767777776666766666666677777777777666666677777777777777777777777777777777777777777777777777777777777777777
        6666677777666666677777777777777777777666667777777666666777776677767666666666777777777777666666677777777777777777777777777777777777777777777777777777777777777777
        6667766666666676777777777777777777776666666777776666666777776667777666677777777777777777766666667777777777777777777777777777777777777777777777766677777777777777
        6666666666666667777777777766666666777777776777777766677767776666677666667777777777777777766666666777777777777777777777777777777777777777777776676677777777777777
        6777766667766667777777777777766667777777666777777777777777777666766776667777777777777777777777676666677777777777777777777777777777667766677766677777777777777777
        6777766666677777777777777777766777777666777777777777777777777777666667777777777777777777777777776667666677777777777767777777777777666767677666777777777777777777
        6777777777777777777777777777766666666777777777777667777777766777766666677777777777777777777777776776666667777777777776777777777777777666666666777777777777777777
        7777777777777777777777777777777666666667777777777777766667776666677777777777777777777777777777777666677776777777777777777777777777777777766677777777777777777777
        777777777777777777777777777777777777777777777777777777767777666666666666666777777777777777777777776667667767777777777667777777777777777776777777666677777777777f
        777777777667677777777777777777777777777777777777777767677777766666666666666677777777777777777766677777666667776666677776666667766777776666777777777766777777766f
        777777777776677777777777777777777777777777777777777767766666667666666666666677777777777766777766667677766666767766667666677776666667767767777777777777777776666f
        77777777776677777777777777777777777777666677777777766767666666676676666666666776677777766677676666677667766777777777777676667677766667666777777777777777776766ff
        7777777766666677777777777777777777777676666677777776667676666666766677766666677777777766666776666667666667767676667766766776677776677676777666666666677776766fff
        777777777666666777777777777777777777666667777777766667766766667776766677777777777777766666777666666766666667767666667767777667777777767777777666666666666666ffff
        7777777666666776677777776777777777776666677777766666677666766667f7777777777777777777666777776666677766666667777666666677777767777777767776776666666fff7fffffffff
        7777777666666677677776666777777777776766667777676666777766777667fffff777777777777777667777776766676766666666667776666777777667777777767776776666766fff7fffffffff
        777777666666666766666666667777777777766666777666766677fff666777fffffffff6677777777777777777677776767766666667676677776667777777777776777767766666f6fff76ffffffff
        77777766666667777666666666667777777776777677667766677ffff76677f7777ffffff6666667777777777777fff77767766666667666677666666777777777776777767767666f6fff76ffffffff
        77777777766667777767666666666677777776776666666666777ffff7667ffff777fffffffff6666777777777f7fff767777666666676766666666666777767777767777677666f76ffff76ffffffff
        7777777776666777776677766666666667766666766767776767cffff7667ffff77f77ffffffff676777777777f7ff7777777676666667766666666697777767777767777677776f76ffff76ffffffff
        7777776666676666777766677766666766666766667677767767ffffff667ffff77ff7777fffff67677777777fffff7767977666766666766666667996977767777767777767766f66ffff76ffffffff
        77776666667776766777776666666666667666767667777676ffffffff767ffff77fff767ffff767677777777ffff7776797769667999699999999999667766677776777776777ff6fffff76ffffffff
        77666666666677666677776766666666676676676767776777ffffffff777fff76ffffc777777767777777667ffff7777697766696999669999999999667966697776777776777f76fffff76ffffffff
        7666666666777767766677766767666677776666666777777cffcccccc7776cc767ccccc76677c77677776667ffff7679697769996776699999999999667666677776777776777f766ffff76ffffffff
        7766666777777676667666777766666677766677777777777ccccccccc7776cc777ccccc777cc677677776697ccff7676697769999999679999999999966666677776777776777f76fffff76ffffffff
        7777777777776766676767677776666667766777777777767ccccccccc7776c777ccccccccccc667677776697ccff7799697769999999679999999999969666777776777766777766fffff76ffffffff
        7777777777767667777666677777766666777777777777767ccccccccc76766777ccccccccccc667677776997cccc779669776999999969999199999999966677776777776677776ffffff76ffffffff
        777776777776677777766667777777777667777777777777cccccccccc777c6777ccccccccccc667677776997ccc777969977699999996991111111999996667777677777667777fffffff76ffffffff
        77777677776677777766ff66777777777767777777777777cccc77777c7776677cccccccccccc666777776997cc7777669977699999996711111111199999667777777777766777fffffff76ffcccccc
        777766777677777776666f66777777777766677777777777c777777777777667ccccccccccccc676777777997cc776769997669999999671111111119999766677777777776677fffffffff6cccccccc
        7777667666776667766ff6f6666777777776666777777777777777777777766cccccccccccccc67677777799ccc777699997699999996671111111111997766677777777777677fccccccc76cccccccc
        7776766777776777676fff66666777777777766677777777766676667777766ccccccccccccc677677777777cc77666999976999999967711111111119777696777777777776677ccccccc76cccccccc
        776766777776777766fffff666777777777767777667777776676667777776c6ccccccccccc6677677777777cc77669999996999999967111111111199777696777777777777677ccccccc76cccccccc
        776776777776777676ffffff66667777777767777767777776766776667776c6ccccccccccc6677677767777cc776999999769999199671111111111167766967777777767776677cccccc76cccccccc
        7767667777777766f6ffffffff66677777776777777677777766776667c766c6ccccccccccc6666777767777cc6679999997699999916711111111111777666677777777677766777ccccc76cccccccc
        776666777777776f6fffffffff66677677777677777677777677677777c7666ccccccccccc66676777667776776799999997999199916711111111111777666677777677676666777ccccc76cccccccc
        77666677776766667fffffffff666776777776767777777777777cccccc7666ccccccccccc66776777667776776799999919799999116711111111111777666677676677766666777ccccc76cccccccc
        776667776767667f7ffccccfff6767767777777677777777777cccc66c6766ccccccccccc666776777667776776999999919999999116711111111111777666677676777766666777ccccc76cccccccc
        77666767666f77777ccccccccc67677677777777677677777cccccc6667676ccccccccccc666776777667776776999999999919991116711111111111777666676776777766666777ccccc76cccccccc
        776667677fff777777cccccccc6777767777777776767777777cccc666766cccccccccccc777776777667776779999999999991991116711111111111777666676776777766666777ccccc76cccccccc
        776767666ccc77766777777ccc6777767777777776767777777cccc6667c7ccccccccccc67777767776677767799999999999179111167111111111177776666767767777666667777cccc76cccccccc
        776767667cccc777777777777c6777767777776776767777777cccc66c7c7cccccccccc676777767776677777799999999999177711167111111111177766667767767776666767777cccc76cccccccc
        776766667cccc77677cc7777676777767777776776767777777cccc6677c7cccccccccc677777777776677777799999999999777779117111111111767766667767767776666767777cccc76cccccccc
        776766767cccccc7c7cccccc776777767777776776767777777cccc6c77c7cccccccccc677777777776677977799999999997991777991111111111767766667667776776666667767cccc76cccccccc
        776766767cccccccccccccccc66777767777776777676777777ccc66c77c7cccccccccc7777777777766779777999999991999977777799777711176677666676777767766766677667ccc76cccccccc
        77676667ccccccccccccccccc66777767777776777676777777ccc66c77c7ccccccccc67777777777766799777999999999996666677779776771176697666776777767766666677667cc7c6cccccccc
        77676667ccccccccccccccccc667777677777767776767777776c6c6c77c7cccccccc666767777777766799777999999919991666677777677111176696766776677776766666676667cc76ccccccccc
        77667677ccccccccccccccccc6677776777777677767677777766cc6c77cccccccccc676777777777767779777999999999991111117777761111176796766776667776766666676667cc76ccccccccc
        77667677ccccccccccccccccc6677776777777677767677777766c6cc7ccccccccccc676777777777777679979999999999911111111177777111766976766776667776776666676667cc76ccccccccc
        7766767cccccccccccccccccc6677776777777677767777777766c6cc7cccccccccc6776777777777776679977699999999911111111777771977777976766776667776776666676667cc76ccccccccc
        7766767cccccccccccccccccc667777677777767776777777776cc6cc7ccccccccccc776777777777776679977699999999111119677776677797767976766777667777776666676667cc76ccccccccc
        7766667ccccccccccccccccccc67777777777767776777777766c6cc77ccccccccccc776777777777776679977699999991111199777776617799677976666777667777776666676667cc7c6cccccccc
        7766767ccccccccccccccccccc6777777777776777677777776c6ccc77ccccccccccc776777776777776679977699977791111699777176611779679776667777667777776766776667cc7c6cccccccc
        776677cccccccccccccccccccc67777677777767776777777766ccc77ccccccccccc7766777777777777679977666669999999997761117711177679776767776667777776776766667cc7c6cccccccc
        77667ccccccccccccccccccccc67777677777767776777777766ccc77cccccccc7776777777777777777679977767766999977777611111111177779977767776677777776777766667cc666cccccccc
        77667ccccccccccccccccccccc6777767777776777677777766cccc77ccccc7776777cccc77777777777777777777777777667771611111111177779977767776677777776777766667cc6c6cccccccc
        776677cccccccccccccccccccc6777767777776777677777667cccc77ccccc7667cccccc677777777777677977777777677666666111111111176799977767776677777776777766667cc666cccccccc
        7766cc7ccccccccccccccccccc6777767777767777677776666cccc77ccccc767ccccc66677776777777677997776777796711111111111111166799977767776677777776777766667ccc66cccccccc
        7766cc7ccccccccccccccccccc6777767777767777677776676cccc77ccccc77ccccc666777776777777677997777766666111111111111111167799977777776776777776777766667ccc66cccccccc
        7766ccc7cccccccccccccccccc67776777777677776777677766ccc77ccccc7cccccc666777776777777677797779776661111111111111111767799977777776777677776677766667ccc66cccccccc
        7766cccc7ccccccccccccccccc67776777777677776777677776ccc77ccccc7ccccccc67777776777777677799779661791111111111111111677799977767777777677777677766667ccc7ccccccccc
        7766ccccc7cccccccccccccccc67776777777677776776677776cccc7ccccccccccccc67777767777777676699776691191111111111111111667799977767777777677777677766667ccc7ccccccccc
        7766ccccc7cccccccccccccccc67767777777677776777677776cccc7ccccccccccccc67777767777777676699766999199911111111111111667799977767777777677777677666667ccc7ccccccccc
        7766cccccc7ccccccccccccccc677677777776777767776777766cc7ccccccccccccc667777767777777677667977999199911111111111111677779977767777777677777677666667ccc7ccccccccc
        7766ccccccc7cccccccccccccc677677777776777767776777766cc7cccccccccccc6677777767777777677799977999199911111111111111676679777767777777677777677666667ccc7ccccccccc
        7766cccccccc7ccccccccccccc677677777776777677776777766cc7cccccccccccc6677777767777777677777777999199911111111111119676777777767777777677777767666667ccc7bcccccccc
        7766ccccccccc7ccccccccccc766767777777777777777677776cc7ccccccccccccc6777777767777777677777777999991911111111111111176777777767777777677777767666667ccc7bcccccccc
        7766cccccccccc77ccccccccc766767777777777777777677776cc7ccccccccccccc6777777767777777777766777991991911111111111111177777777677777777677777777666667ccc7bbbcccccc
        7766cccccccccccc7cccccccc766767777777777777777677766cc7cccccccccccc66777777667777777779966777991991911111111111111677777777677777777677777777666667ccc7bbbcccccc
        77666cccccccccccbbbcccccc766767777777777777777776766ccccccccccccccc67777777677777677779966666791991991111111111111677777777677777777677777776766667ccc7bbbcccccc
        77666cccccccbbbbbbccccccc767767777777777776777776766cccccccbbbbcccc67777777677777667779967676799999991111111111111967766777676777777677777776766667ccc7bbbcccccc
        77666cccccccbbbbb7bbcbccc767767776677777776777776766cc7ccccbbbbbbb6677777776777777677999676767999999191111111111116676767776767777776777777767666667cc7bbbcccccc
        77666cccccccbbbbb7bbbcccc767767766777777776777776666cc7cccbbbbbbbb6677777776777777677999676766799999991111111111116676767776767777776777777767766667cc7bbccccccc
        77666cccccccbbbbb7bbbbc66667767766777677776777776666c7ccccbbbbbbbb6677777767777777677999966776791999991111111111116777777776767777776777777767766667cc7bbccccccc
        77666cccccccbbbbb7bbbbc66667677766777677776777776666c7ccccbbbbbbbbb677777767777777679799976676699199199911111111167777777776767777776777777767766667cc7bbccccccc
        77666cccccccbbbbb7bbbbc6676767766677767777677776766cc7ccccc7bbbbbbb677777677777777679799997667697199199911111119967777777777767777776776777767766667cc7bcccccccc
        77666cccccccbbbbbb7bbbc7676767766677766777677776766667ccccc76bbb666677777777777777677779999766669999119911111119677777777777767777776776777777766666cc7bcccccccc
        776666ccccccbbbbbb7bbb66677677666777766677677776766b666ccccc66bb666777777777777777677779999976667991999911111999677776777777767777777776777767766666cc7ccccccccc
        7776666cccccbbbbbbb7bb667767776667776677676777767677776cccccc6bb666777777767777776777677999996676999911999999966777776777777767777777776777776766666cc7ccccccccc
        7776666cccccbbbbbbb7bb667767776667776777677777767677776ccc6666bb6667777777677777767766699999999766999919999119977767677777777677777777776777767766666c7ccccccccc
        7776666cccccbbbbbbb7b76677677666777677776777777666666666cc666ccb6677777766677776677666699979999766999999999196997767677677777677767767776777767766676c7ccccccccc
        7776666ccccccbbbbbb7b766776776667767777767767776667776ccc6676ccc6777777766677776677666699979999776999999999999997677677677777677767767777677766776666c7ccccccccc
        7777666cccccccbbbbb777667767666677677777677677766677776666666ccc67777777666777767776666699999997767119991999997976767776777776777677767777677666767666cccccccccc
        7777666cccccccbbbbb77767766766667767777767767766667777767766ccccc77777776667777676666666999999977679999999999797677677767777767776677677776776667666667ccccccccc
        7777676ccccccccbbbb76667776666667777777677767666667777776766ccccc77777776667777666666666699999997679911999999976777777767777767776677677776776666666666c6ccccccc
        7777777ccccccccbbbb77677767666667777777677667666677777777766ccccc7777777676777766776667669779997976999999999976777777676777776777667776777767666666666666ccccccc
        7776777cccccccbcbb7bb677667666667777777677776666677777777776cccc677777766677777667676666666677799769999999997677777766767777767776777767777676666667666666cccccc
        77767776ccccc77c77bb6777677666667777777677776766666666677776cccc6777777676777776767676667666779767699999997766767776667777776777767777766776666666677666666ccccc
        77767776777c7ccccbb7676677766666777777776777767676666666677cccc777777776667777767666666676666697769999999777676777666677777767777677777767776666666777666666cccc
        777767776bcccccccccc776777666666777777776777767677666776666cccc7777777766777777666777766667777799696677777767677766666777777677776677777667776666667676666666ccc
        777767776cccccccb76776666666666677777777677666777767667767677c677777776766767777667776677699977666677777776667777667777777776777666777777677766667776766676676cc
        777777776cccccb777677766666666767777777776767777777777677667767777777767776677777677777666997666677666777677777776677777777767766667777776777667766766666776666c
        7777767766cccb77667776666666666677777667766667777777777666666677777766777776777777677776699776677766666667777777677777777666776666677777767666666667666766766666
        77777667666cb766666666666666667777666677766677777777777766666777776777667766777777667777997667777799777977777777677666676666666666667777767766666667666676667666
        7777766777667766667766666666667776666677766667777777777776667777767777666677777777777777777779999997779776776667666676666677766677767777767777776666666666666666
        7777766677666667677666666666666666676666666667667667777776667767777666667777777676767777777699999977797777777777777776667776666677767777767767777677777776666666
        7777766777666777666666666667676666666666666667666777677666667776667667666666777777777777777776777779977777767777776666777767766777766677777767777677777777666666
        6666666777766777666666666666667666777767777777666677776666767667776667676666667777767766677777767796667776666666666667777677766667777667777777777766677777777666
        6666666677776776666666666666666699666777777667799777777666676666666666766677776767776776666666669999667666666666667777777677666777777767776767777766777777777766
        ffffff6ff77766666666666699fffffffffffff999ffffffffffff7fffffff999999996677777777777777776999999999997777777777766677777776667777777777677776667777666f7777777777
        ffffff6fff666667777ffffffff999fffffffffffffff9ffffff9999ffffffffffff96666666666667776777799999999997777997777777f777777fffff7777776777767776667777776fff77777777
        ffffffffff666667ffffffffffffffffffffffffffffffffffffffffffffff99f9996666ffffff9999777777777999999977777777777777777777ffff777fffffff6776777666f777777ffffff77777
        ffffffff666666ffffffffffffffffffffff99ff99fffffffff9ff99fffff9ff9ff66666fffffffffffff777f77fffffff7fff777fff9f667776fffffffffffffffffff7777766f7777777fffffff777
        ffffffff666ffffffffffffffffffffffffffffffffffffffffffffffffffffff669ffff999999fffffffff77fff9999ffffffffffffffff7ffffffffffffffffffffffff777ff6777f777ffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff99999ff99ff666ffff9fffff99fff9999999999fffffffff99999ffffffffffffffffffffffffffffffffff6667fffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffff999999999969999999999fffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffff999ffffffffff99ffff9999999ffffffffffffffff9ffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff99999ffffffffffffffffffffffffffffffffffffffffffffff9fffffffff99ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99999fffffffffffffffff99fff999ffffffffffffff999999fffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff999f9999999ff999ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99fff99999999fffffff999999ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9999999999ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
"""))
pause(2000)
game.show_long_text("近幾年來每當到了凌晨", DialogLayout.BOTTOM)
game.show_long_text("森林裡出現超自然現象", DialogLayout.BOTTOM)
game.show_long_text("通向外星人所在地的傳送門", DialogLayout.BOTTOM)
game.show_long_text("探險家得知此消息後", DialogLayout.BOTTOM)
game.show_long_text("去尋找從未找的外星人寶藏", DialogLayout.BOTTOM)
game.show_long_text("根據幾百年前發現的寶藏圖", DialogLayout.BOTTOM)
game.show_long_text("敘述必須湊齊鑰匙碎片", DialogLayout.BOTTOM)
game.show_long_text("就能打開遺跡的大門", DialogLayout.BOTTOM)
scene.set_background_image(img("""
    666676777777777777777777777777777777777777777777777777776777766666666666666667777777666666666677777777777777777777777777777777777777777777777777777777777777777c
        6666667777777777776677777777777777777777777777777777777767777776666766666666677777777777666666677777777777777777777777777777777777777777777777777777777777777777
        6666677777666666677777777777777777777666667777777666666777776677767666666666777777777777666666677777777777777777777777777777777777777777777777777777777777777777
        6667766666666676777777777777777777776666666777776666666777776667777666677777777777777777766666667777777777777777777777777777777777777777777777766677777777777777
        6666666666666667777777777766666666777777776777777766677767776666677666667777777777777777766666666777777777777777777777777777777777777777777776676677777777777777
        6777766667766667777777777777766667777777666777777777777777777666766776667777777777777777777777676666677777777777777777777777777777667766677766677777777777777777
        6777766666677777777777777777766777777666777777777777777777777777666667777777777777777777777777776667666677777777777767777777777777666767677666777777777777777777
        6777777777777777777777777777766666666777777777777667777777766777766666677777777777777777777777776776666667777777777776777777777777777666666666777777777777777777
        7777777777777777777777777777777666666667777777777777766667776666677777777777777777777777777777777666677776777777777777777777777777777777766677777777777777777777
        777777777777777777777777777777777777777777777777777777767777666666666666666777777777777777777777776667667767777777777667777777777777777776777777666677777777777f
        777777777667677777777777777777777777777777777777777767677777766666666666666677777777777777777766677777666667776666677776666667766777776666777777777766777777766f
        777777777776677777777777777777777777777777777777777767766666667666666666666677777777777766777766667677766666767766667666677776666667767767777777777777777776666f
        77777777776677777777777777777777777777666677777777766767666666676676666666666776677777766677676666677667766777777777777676667677766667666777777777777777776766ff
        7777777766666677777777777777777777777676666677777776667676666666766677766666677777777766666776666667666667767676667766766776677776677676777666666666677776766fff
        777777777666666777777777777777777777666667777777766667766766667776766677777777777777766666777666666766666667767666667767777667777777767777777666666666666666ffff
        7777777666666776677777776777777777776666677777766666677666766667f7777777777777777777666777776666677766666667777666666677777767777777767776776666666fff7fffffffff
        7777777666666677677776666777777777776766667777676666777766777667fffff777777777777777667777776766676766666666667776666777777667777777767776776666766fff7fffffffff
        777777666666666766666666667777777777766666777666766677fff666777fffffffff6677777777777777777677776767766666667676677776667777777777776777767766666f6fff76ffffffff
        77777766666667777666666666667777777776777677667766677ffff76677f7777ffffff6666667777777777777fff77767766666667666677666666777777777776777767767666f6fff76ffffffff
        77777777766667777767666666666677777776776666666666777ffff7667ffff777fffffffff6666777777777f7fff767777666666676766666666666777767777767777677666f76ffff76ffffffff
        7777777776666777776677766666666667766666766767776767cffff7667ffff77f77ffffffff676777777777f7ff7777777676666667766666666697777767777767777677776f76ffff76ffffffff
        7777776666676666777766677766666766666766667677767767ffffff667ffff77ff7777fffff67677777777fffff7767977666766666766666667996977767777767777767766f66ffff76ffffffff
        77776666667776766777776666666666667666767667777676ffffffff767ffff77fff767ffff767677777777ffff7776797769667999699999999999667766677776777776777ff6fffff76ffffffff
        77666666666677666677776766666666676676676767776777ffffffff777fff76ffffc777777767777777667ffff7777697766696999669999999999667966697776777776777f76fffff76ffffffff
        7666666666777767766677766767666677776666666777777cffcccccc7776cc767ccccc76677c77677776667ffff7679697769996776699999999999667666677776777776777f766ffff76ffffffff
        7766666777777676667666777766666677766677777777777ccccccccc7776cc777ccccc777cc677677776697ccff7676697769999999679999999999966666677776777776777f76fffff76ffffffff
        7777777777776766676767677776666667766777777777767ccccccccc7776c777ccccccccccc667677776697ccff7799697769999999679999999999969666777776777766777766fffff76ffffffff
        7777777777767667777666677777766666777777777777767ccccccccc76766777ccccccccccc667677776997cccc779669776999999969999199999999966677776777776677776ffffff76ffffffff
        777776777776677777766667777777777667777777777777cccccccccc777c6777ccccccccccc667677776997ccc777969977699999996991111111999996667777677777667777fffffff76ffffffff
        77777677776677777766ff66777777777767777777777777cccc77777c7776677cccccccccccc666777776997cc7777669977699999996711111111199999667777777777766777fffffff76ffcccccc
        777766777677777776666f66777777777766677777777777c777777777777667ccccccccccccc676777777997cc776769997669999999671111111119999766677777777776677fffffffff6cccccccc
        7777667666776667766ff6f6666777777776666777777777777777777777766cccccccccccccc67677777799ccc777699997699999996671111111111997766677777777777677fccccccc76cccccccc
        7776766777776777676fff66666777777777766677777777766676667777766ccccccccccccc677677777777cc77666999976999999967711111111119777696777777777776677ccccccc76cccccccc
        776766777776777766fffff666777777777767777667777776676667777776c6ccccccccccc6677677777777cc77669999996999999967111111111199777696777777777777677ccccccc76cccccccc
        776776777776777676ffffff66667777777767777767777776766776667776c6ccccccccccc6677677767777cc776999999769999199671111111111167766967777777767776677cccccc76cccccccc
        7767667777777766f6ffffffff66677777776777777677777766776667c766c6ccccccccccc6666777767777cc6679999997699999916711111111111777666677777777677766777ccccc76cccccccc
        776666777777776f6fffffffff66677677777677777677777677677777c7666ccccccccccc66676777667776776799999997999199916711111111111777666677777677676666777ccccc76cccccccc
        77666677776766667fffffffff666776777776767777777777777cccccc7666ccccccccccc66776777667776776799999919799999116711111111111777666677676677766666777ccccc76cccccccc
        776667776767667f7ffccccfff6767767777777677777777777cccc66c6766ccccccccccc666776777667776776999999919999999116711111111111777666677676777766666777ccccc76cccccccc
        77666767666f77777ccccccccc67677677777777677677777cccccc6667676ccccccccccc666776777667776776999999999919991116711111111111777666676776777766666777ccccc76cccccccc
        776667677fff777777cccccccc6777767777777776767777777cccc666766cccccccccccc777776777667776779999999999991991116711111111111777666676776777766666777ccccc76cccccccc
        776767666ccc77766777777ccc6777767777777776767777777cccc6667c7ccccccccccc67777767776677767799999999999179111167111111111177776666767767777666667777cccc76cccccccc
        776767667cccc777777777777c6777767777776776767777777cccc66c7c7cccccccccc676777767776677777799999999999177711167111111111177766667767767776666767777cccc76cccccccc
        776766667cccc77677cc7777676777767777776776767777777cccc6677c7cccccccccc677777777776677777799999999999777779117111111111767766667767767776666767777cccc76cccccccc
        776766767cccccc7c7cccccc776777767777776776767777777cccc6c77c7cccccccccc677777777776677977799999999997991777991111111111767766667667776776666667767cccc76cccccccc
        776766767cccccccccccccccc66777767777776777676777777ccc66c77c7cccccccccc7777777777766779777999999991999977777799777711176677666676777767766766677667ccc76cccccccc
        77676667ccccccccccccccccc66777767777776777676777777ccc66c77c7ccccccccc67777777777766799777999999999996666677779776771176697666776777767766666677667cc7c6cccccccc
        77676667ccccccccccccccccc667777677777767776767777776c6c6c77c7cccccccc666767777777766799777999999919991666677777677111176696766776677776766666676667cc76ccccccccc
        77667677ccccccccccccccccc6677776777777677767677777766cc6c77cccccccccc676777777777767779777999999999991111117777761111176796766776667776766666676667cc76ccccccccc
        77667677ccccccccccccccccc6677776777777677767677777766c6cc7ccccccccccc676777777777777679979999999999911111111177777111766976766776667776776666676667cc76ccccccccc
        7766767cccccccccccccccccc6677776777777677767777777766c6cc7cccccccccc6776777777777776679977699999999911111111777771977777976766776667776776666676667cc76ccccccccc
        7766767cccccccccccccccccc667777677777767776777777776cc6cc7ccccccccccc776777777777776679977699999999111119677776677797767976766777667777776666676667cc76ccccccccc
        7766667ccccccccccccccccccc67777777777767776777777766c6cc77ccccccccccc776777777777776679977699999991111199777776617799677976666777667777776666676667cc7c6cccccccc
        7766767ccccccccccccccccccc6777777777776777677777776c6ccc77ccccccccccc776777776777776679977699977791111699777176611779679776667777667777776766776667cc7c6cccccccc
        776677cccccccccccccccccccc67777677777767776777777766ccc77ccccccccccc7766777777777777679977666669999999997761117711177679776767776667777776776766667cc7c6cccccccc
        77667ccccccccccccccccccccc67777677777767776777777766ccc77cccccccc7776777777777777777679977767766999977777611111111177779977767776677777776777766667cc666cccccccc
        77667ccccccccccccccccccccc6777767777776777677777766cccc77ccccc7776777cccc77777777777777777777777777667771611111111177779977767776677777776777766667cc6c6cccccccc
        776677cccccccccccccccccccc6777767777776777677777667cccc77ccccc7667cccccc677777777777677977777777677666666111111111176799977767776677777776777766667cc666cccccccc
        7766cc7ccccccccccccccccccc6777767777767777677776666cccc77ccccc767ccccc66677776777777677997776777796711111111111111166799977767776677777776777766667ccc66cccccccc
        7766cc7ccccccccccccccccccc6777767777767777677776676cccc77ccccc77ccccc666777776777777677997777766666111111111111111167799977777776776777776777766667ccc66cccccccc
        7766ccc7cccccccccccccccccc67776777777677776777677766ccc77ccccc7cccccc666777776777777677797779776661111111111111111767799977777776777677776677766667ccc66cccccccc
        7766cccc7ccccccccccccccccc67776777777677776777677776ccc77ccccc7ccccccc67777776777777677799779661791111111111111111677799977767777777677777677766667ccc7ccccccccc
        7766ccccc7cccccccccccccccc67776777777677776776677776cccc7ccccccccccccc67777767777777676699776691191111111111111111667799977767777777677777677766667ccc7ccccccccc
        7766ccccc7cccccccccccccccc67767777777677776777677776cccc7ccccccccccccc67777767777777676699766999199911111111111111667799977767777777677777677666667ccc7ccccccccc
        7766cccccc7ccccccccccccccc677677777776777767776777766cc7ccccccccccccc667777767777777677667977999199911111111111111677779977767777777677777677666667ccc7ccccccccc
        7766ccccccc7cccccccccccccc677677777776777767776777766cc7cccccccccccc6677777767777777677799977999199911111111111111676679777767777777677777677666667ccc7ccccccccc
        7766cccccccc7ccccccccccccc677677777776777677776777766cc7cccccccccccc6677777767777777677777777999199911111111111119676777777767777777677777767666667ccc7bcccccccc
        7766ccccccccc7ccccccccccc766767777777777777777677776cc7ccccccccccccc6777777767777777677777777999991911111111111111176777777767777777677777767666667ccc7bcccccccc
        7766cccccccccc77ccccccccc766767777777777777777677776cc7ccccccccccccc6777777767777777777766777991991911111111111111177777777677777777677777777666667ccc7bbbcccccc
        7766cccccccccccc7cccccccc766767777777777777777677766cc7cccccccccccc66777777667777777779966777991991911111111111111677777777677777777677777777666667ccc7bbbcccccc
        77666cccccccccccbbbcccccc766767777777777777777776766ccccccccccccccc67777777677777677779966666791991991111111111111677777777677777777677777776766667ccc7bbbcccccc
        77666cccccccbbbbbbccccccc767767777777777776777776766cccccccbbbbcccc67777777677777667779967676799999991111111111111967766777676777777677777776766667ccc7bbbcccccc
        77666cccccccbbbbb7bbcbccc767767776677777776777776766cc7ccccbbbbbbb6677777776777777677999676767999999191111111111116676767776767777776777777767666667cc7bbbcccccc
        77666cccccccbbbbb7bbbcccc767767766777777776777776666cc7cccbbbbbbbb6677777776777777677999676766799999991111111111116676767776767777776777777767766667cc7bbccccccc
        77666cccccccbbbbb7bbbbc66667767766777677776777776666c7ccccbbbbbbbb6677777767777777677999966776791999991111111111116777777776767777776777777767766667cc7bbccccccc
        77666cccccccbbbbb7bbbbc66667677766777677776777776666c7ccccbbbbbbbbb677777767777777679799976676699199199911111111167777777776767777776777777767766667cc7bbccccccc
        77666cccccccbbbbb7bbbbc6676767766677767777677776766cc7ccccc7bbbbbbb677777677777777679799997667697199199911111119967777777777767777776776777767766667cc7bcccccccc
        77666cccccccbbbbbb7bbbc7676767766677766777677776766667ccccc76bbb666677777777777777677779999766669999119911111119677777777777767777776776777777766666cc7bcccccccc
        776666ccccccbbbbbb7bbb66677677666777766677677776766b666ccccc66bb666777777777777777677779999976667991999911111999677776777777767777777776777767766666cc7ccccccccc
        7776666cccccbbbbbbb7bb667767776667776677676777767677776cccccc6bb666777777767777776777677999996676999911999999966777776777777767777777776777776766666cc7ccccccccc
        7776666cccccbbbbbbb7bb667767776667776777677777767677776ccc6666bb6667777777677777767766699999999766999919999119977767677777777677777777776777767766666c7ccccccccc
        7776666cccccbbbbbbb7b76677677666777677776777777666666666cc666ccb6677777766677776677666699979999766999999999196997767677677777677767767776777767766676c7ccccccccc
        7776666ccccccbbbbbb7b766776776667767777767767776667776ccc6676ccc6777777766677776677666699979999776999999999999997677677677777677767767777677766776666c7ccccccccc
        7777666cccccccbbbbb777667767666677677777677677766677776666666ccc67777777666777767776666699999997767119991999997976767776777776777677767777677666767666cccccccccc
        7777666cccccccbbbbb77767766766667767777767767766667777767766ccccc77777776667777676666666999999977679999999999797677677767777767776677677776776667666667ccccccccc
        7777676ccccccccbbbb76667776666667777777677767666667777776766ccccc77777776667777666666666699999997679911999999976777777767777767776677677776776666666666c6ccccccc
        7777777ccccccccbbbb77677767666667777777677667666677777777766ccccc7777777676777766776667669779997976999999999976777777676777776777667776777767666666666666ccccccc
        7776777cccccccbcbb7bb677667666667777777677776666677777777776cccc677777766677777667676666666677799769999999997677777766767777767776777767777676666667666666cccccc
        77767776ccccc77c77bb6777677666667777777677776766666666677776cccc6777777676777776767676667666779767699999997766767776667777776777767777766776666666677666666ccccc
        77767776777c7ccccbb7676677766666777777776777767676666666677cccc777777776667777767666666676666697769999999777676777666677777767777677777767776666666777666666cccc
        777767776bcccccccccc776777666666777777776777767677666776666cccc7777777766777777666777766667777799696677777767677766666777777677776677777667776666667676666666ccc
        777767776cccccccb76776666666666677777777677666777767667767677c677777776766767777667776677699977666677777776667777667777777776777666777777677766667776766676676cc
        777777776cccccb777677766666666767777777776767777777777677667767777777767776677777677777666997666677666777677777776677777777767766667777776777667766766666776666c
        7777767766cccb77667776666666666677777667766667777777777666666677777766777776777777677776699776677766666667777777677777777666776666677777767666666667666766766666
        77777667666cb766666666666666667777666677766677777777777766666777776777667766777777667777997667777799777977777777677666676666666666667777767766666667666676667666
        7777766777667766667766666666667776666677766667777777777776667777767777666677777777777777777779999997779776776667666676666677766677767777767777776666666666666666
        7777766677666667677666666666666666676666666667667667777776667767777666667777777676767777777699999977797777777777777776667776666677767777767767777677777776666666
        7777766777666777666666666667676666666666666667666777677666667776667667666666777777777777777776777779977777767777776666777767766777766677777767777677777777666666
        6666666777766777666666666666667666777767777777666677776666767667776667676666667777767766677777767796667776666666666667777677766667777667777777777766677777777666
        6666666677776776666666666666666699666777777667799777777666676666666666766677776767776776666666669999667666666666667777777677666777777767776767777766777777777766
        ffffff6ff77766666666666699fffffffffffff999ffffffffffff7fffffff999999996677777777777777776999999999997777777777766677777776667777777777677776667777666f7777777777
        ffffff6fff666667777ffffffff999fffffffffffffff9ffffff9999ffffffffffff96666666666667776777799999999997777997777777f777777fffff7777776777767776667777776fff77777777
        ffffffffff666667ffffffffffffffffffffffffffffffffffffffffffffff99f9996666ffffff9999777777777999999977777777777777777777ffff777fffffff6776777666f777777ffffff77777
        ffffffff666666ffffffffffffffffffffff99ff99fffffffff9ff99fffff9ff9ff66666fffffffffffff777f77fffffff7fff777fff9f667776fffffffffffffffffff7777766f7777777fffffff777
        ffffffff666ffffffffffffffffffffffffffffffffffffffffffffffffffffff669ffff999999fffffffff77fff9999ffffffffffffffff7ffffffffffffffffffffffff777ff6777f777ffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff99999ff99ff666ffff9fffff99fff9999999999fffffffff99999ffffffffffffffffffffffffffffffffff6667fffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffff999999999969999999999fffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffff999ffffffffff99ffff9999999ffffffffffffffff9ffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff99999ffffffffffffffffffffffffffffffffffffffffffffff9fffffffff99ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99999fffffffffffffffff99fff999ffffffffffffff999999fffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff999f9999999ff999ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99fff99999999fffffff999999ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9999999999ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
"""))
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
animation.run_image_animation(mySprite,
    [img("""
            . . . . . . f f f f f f . . . . 
                . . . . f f b b b b b b f . . . 
                . . . f f b b b b c b c c f f . 
                . . . f b b b b b b b b b b b f 
                . . f f f f f f f f f f f f f f 
                . . . f e 6 e e e e e e e e f . 
                . . f f e 6 e d d 1 f d e e f . 
                . . f e e 6 d d d 1 f d d f f . 
                . . f e e f d d d d d d 3 f . . 
                . f e e e f 9 9 9 9 9 9 9 f . . 
                . f f f f f 9 9 9 f 9 9 f f . . 
                . . . . f f f d d f 9 9 f . . . 
                . . . . f b f f f f c c f . . . 
                . . . . . f b b b b b b f . . . 
                . . . . . . f f f f f f . . . . 
                . . . . . . . f f f . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . f f f f f . . . . . 
                . . . . f f b b b b b f f . . . 
                . . . f f b b b b b b b b f . . 
                . . . f b b b b b c b c c f f . 
                . . f f b b b b b b b b b b b f 
                . f f f f f f f f f f f f f f f 
                . . f e e 6 e e e e e e e f f . 
                . . f e e 6 d d d 1 f d e e f . 
                . . f e f d d d d 1 f d d f . . 
                . . f e f d d d d d d d 3 f . . 
                . . f e f f 9 9 9 9 9 9 f f . . 
                . . . f . f 9 9 9 f 9 9 f . . . 
                . . . . f c f d d f c c f f . . 
                . . . . f f f f f f f f f f . . 
                . . . . . f f . . . f f f . . .
        """)],
    200,
    True)
mySprite.set_position(1, 94)
mySprite.set_velocity(31, 0)

def on_on_update():
    global p1, mySprite2
    if mySprite.x >= 100:
        animation.run_image_animation(mySprite,
            [img("""
                    . . . . . . f f f f f f . . . . 
                                . . . . f f b b b b b b f . . . 
                                . . . f f b b b b c b c c f f . 
                                . . . f b b b b b b b b b b b f 
                                . . f f f f f f f f f f f f f f 
                                . . . f e 6 e e e e e e e e f . 
                                . . f f e 6 e d d 1 f d e e f . 
                                . . f e e 6 d d d 1 f d d f f . 
                                . . f e e f d d d d d d 3 f . . 
                                . f e e e f 9 9 9 9 9 9 9 f . . 
                                . f f f f f 9 9 9 f 9 9 f f . . 
                                . . . . f f f d d f 9 9 f . . . 
                                . . . . f b f f f f c c f . . . 
                                . . . . . f b b b b b b f . . . 
                                . . . . . . f f f f f f . . . . 
                                . . . . . . . f f f . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . f f f f f . . . . . 
                                . . . . f f b b b b b f f . . . 
                                . . . f f b b b b b b b b f . . 
                                . . . f b b b b b c b c c f f . 
                                . . f f b b b b b b b b b b b f 
                                . f f f f f f f f f f f f f f f 
                                . . f e e 6 e e e e e e e f f . 
                                . . f e e 6 d d d 1 f d e e f . 
                                . . f e f d d d d 1 f d d f . . 
                                . . f e f d d d d d d d 3 f . . 
                                . . f e f f 9 9 9 9 9 9 f f . . 
                                . . . f . f 9 9 9 f 9 9 f . . . 
                                . . . . f c f d d f c c f f . . 
                                . . . . f f f f f f f f f f . . 
                                . . . . . f f . . . f f f . . .
                """),
                img("""
                    . . . . . . f f f f f f . . . . 
                                . . . . f f b b b b b b f . . . 
                                . . . f f b b b b c b c c f f . 
                                . . . f b b b b b b b b b b b f 
                                . . f f f f f f f f f f f f f f 
                                . . . f e 6 e e e e e e e e f . 
                                . . f f e 6 e d d 1 f d e e f . 
                                . . f e e 6 d d d 1 f d d f f . 
                                . . f e e f d d d d d d 3 f . . 
                                . f e e e f 9 9 9 9 9 9 9 f . . 
                                . f f f f f 9 9 9 f 9 9 f f . . 
                                . . . . f f f d d f 9 9 f . . . 
                                . . . . f b f f f f c c f . . . 
                                . . . . . f b b b b b b f . . . 
                                . . . . . . f f f f f f . . . . 
                                . . . . . . . f f f . . . . . .
                """)],
            100,
            False)
        mySprite.set_velocity(0, 0)
        mySprite.set_position(100, 94)
        scene.set_background_image(img("""
            6666666666666666666666666666666666666cccccc666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666ccccddbbccc6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        666666666666666666666666666666666ccddddbbbbbc6666666666666666666666666666666669666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        666666666666666666666666666666666cddbcbbbbbbdccccc66666666666666666666666999999666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        666666666666666666666666666666666cddbccccbbbdddddcccc66666666666666666966666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        666666666666666666666666666666666ccddbccccbbbddddddddc6666cccc66666666666666666696666666666666666666666666666666666666666666666666666666666666666666666666666666
                        66666666666666666666666666666666ccdddbbbbbbbbdddddddddcccccddcc6666666665566699996666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666ccddddbbbbbbbbbbddddddddddddddbc6666666655776666999666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666ccddddddbbbbbbbbbbbddddddddddbbc6666666557777666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        666666666666666666666666666666ccddddbbbbcccccccccccbbbdddddbbbcc666665566666775666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        666666666666666666666666666666cddddbbbbbcdccccdcccccccdddbbbbbbbccc665666666667555566666666666666666666666666666666666666666666666666666666666666666666666666666
                        666666666666666666666666666666cdddbccccccdbbcdbcccddbbcccbbbbbbbbbccc66ecc66677777776996666666666666666666666666666666666666666666666666666666666666666666666666
                        66666666669666666666666666666cdddcccccccbcccccbcccdbcccccbbbbbbbbbbbc6eeccb6666766666666966666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666ccdccdddddbbccccdcccbcbccdbcccbbbbbbbbbbc6eeccbb667776666667666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666969666666666666666666cdccdddddccccdccccdbbccbcbccbcccbbbbbbbbc6eecccbb667676fff67666666666666666666666666666666666666666666666666666666666996666666666666
                        666666996666666666666666666ccccddddddddddddccccccccbcccdbcdccbbbbbbbc6eeccccbb676766ff67666666666666666666666666666666666666666666666666666666666996666666666666
                        66666696666666666666666666ccccbdddddcdddddddddbcccccdcccccdccbbbbbbbc66ececccbb666767f67666666666666666666666666666666666666666777777766666666669999666666666666
                        6666666666666666666666666cddccdbdddcbddddddcccccdcccccbccccccbbbbbbbc66ececcccbb77767777766666666666666666666666666666666666677777777776666666669999966666666666
                        666666666666666666666666ccddcbbbbddcbbbbbdcbddddddddcccccbccccbbbbcbc666cecfcccbc6677777556666666666666666696666666999999666667776677777766666669999966666666666
                        6666666666666666666666ccddddcbbbbbcbbbbcbbbbbccbbdddddccdbcdccbbbccbc666e66fccfcbb767777556666666666666669696966666999999966666777666777776666699999966666666666
                        6666666666666666666666cddbddcbbbbbcbbccbbcbccccccccccccccbcccbcbbccbc666e6eeccfccc777777755666666666666669969696666699999996666777777666777666699999999666666666
                        6666666666666666666666cdbbddccbbbcbbbbcccccccccbbbddddddbccbcccbbccbc666e6eecffcfcb76777755666669666666699996996666699999999666677777776667766699999999966666666
                        666666666666666666666ccdbbddccbbbcccccccccccccccccbbbdddbccccccbbccbcc666eeeeefcffb77667755666699666666699996999666699999999666677776666676766699999999996666666
                        66666666666666666666cccdbbbbcccbccccccccffccccccccccbbcccdbcccbcbcbbbc666ee666efffc77776755669996669669969999699966669999999666667777777777676699999999999666666
                        66666666666666666666cddcbbbbccccccccccccfcccccccccccccccddbbbcccbbbbbc666ee66eeffcc77776755666996699669966996699966669999999666666677777666676669999999999666666
                        66666666666666666666cddbccccccffccccccffcccfffffcccbbbbbcdddbbcccbddcc666e666eeffccc7776755666999699999996669999966669999996666666666677777766666999999999666666
                        66666666666666666666ccdbbcccccfffcccffccccfffcccccccbbbbbccccbcccddbcc6666666eefffffee77775556699699999999969999966669999996666666666667777767666666666699666666
                        6666696666666666666ccccbbbccccccfffcffccccfffffffccccccbbddddbccdddcc66666666effffffe777775555566699999999969999966669999996666666666666677767666666666666666666
                        666699666666666666ccddccbbccccccfffcffccffffffffffffccccbbbddccccccc6666666666efcffe7777767755556669996999999999966666996666666666666666666767666666666666666666
                        69999666666666666ccddddccbcccccccfffffcfccffccccffffcccccbbddcccc66666666666e6efccee7777677777775666966666999999966666669666eeeeeeeeeeeeee67676ee666666666666666
                        69999666666666666cddbddbcbbcccccccfffffcfffffcccccccccccccbddcc6666666666666e6effcee577767777777556666666699999996666669966eeeeee22222222e67677eeee2226666666666
                        6999966666666666cccbbbbbcbccccfccccffffffffffffffffcccccbbccccc6666666666666eeeffcc557776775777775556666669999999666666966eeee22222222222e676776e222222266666666
                        9699966666666666ddcbbbccccccfcffccffffffffffffccffffcccccbbbcbc66666666666e6eecffcb5777767765555777555669969999996666666eeee2222222222222eee66762222222222266666
                        996966666666666cddbccccddccccfffffffffffffffffccccffcccccbbbcbcc66666666e6e6efcffc5777776777766557775566999666999666666bee22222222222222222ee6766666622222222666
                        996966666666666cddddccddddccccfffffffffffffffffccccffccccbbbccc666666666e6eecfcecb5776666777776677777757699966999666666ee2222222222222222222e6666677766222222222
                        996666666666666cddccddddddccccffffffffffffffffffccccccccccbbccc6666666e6e6eecfccc77767777777777777777777766666699666666ee2222222222222222222ee6eee67667662222222
                        966666666666666cccccdddddbbccccccfffffffffffffffffcccccbbbccccc6666666e6eeefcfccb7667777777777777777777777666666999666eee22222222222222222222e6e2ee6766776222222
                        9666666666666666cccddbbbbbbccccccfffffffffffffffffffccccbbbccc6666666ee66eefcccb7777777776677777777766777776669666666e2222222ee22222222222222eee22ee676677662222
                        6966666666666666ccddbbbbbbbccfffffffffffffffffccffffccccccbbccf6666666ee6efccccb777776666666666677777677777766996666ee2222222e2222222222222222e2222e677666676622
                        699666666666666cccdbbbbbbbbcccfffffffffffffffffcfffffccccccbc1ff6666e66eeefcecb777666666666999996677776777776699996ee22222222e222222222222222222222ee67776677622
                        699666666666666cddddbbbbbbcccccccffffffffffffffccfcfffccccccc11fff66ee6eeffccb777666666666666666666677767777766996eee22222222ee222222222222222222222ee6776777662
                        69966666666666ccddddbbbbbcccccccccffffffffffffffcfccfcccbbccc1111f666eeecffcb7766699999966669699999966667777766666ee222222ee2ee222222e222222222222222e6776767762
                        6996666666666cccddddbbbcccccccccccfffffffffffffffccccccbbbdcffbb1f666eeeccfc77766699999999996699999999676777776666e2222222ee2ee222e222ee2222222222222ee677766762
                        6966666666666ccddddddddbbbbbccfffffffffffffffffcffccccccbddc6ffbb1f666eecccb7766699999999999966666666665777777666e222222222e2eeb222ee222e2222222222222ee66777762
                        6966666666666ccdddddddcbbbbbcccffffffffffffffccfffccccbccddc66ffb1f6666eccc7556669999999999999966999966555777766ee2222222222eeeb2222ee222e2222222222222eee666662
                        6966666666666ccdddddccddbbbbcccccffcfffffffffcccccccccbbccc6666fb11f69eecb75566669999999999999999666699665777766e22222222222eeebbbb22eee22ee2e22222222222eeeee22
                        6966666666666ccdddcccddbbbbbccccccccfffffccffccccccccbbbdcc66669fbbffffee555666699999999999999999999666667777766e222222222222eebeebb222eee22eeee2222222222222222
                        6696666666666ccccccddddbbbbbcbcccccfffffcccfcfccccccccbdddc666699fb1ff11e55561ff999999999ffffffffffff99967777766e222222222222eb444ebb2222e22222eee22222222222222
                        66699996666666ccccdddbbbbbbcbbccccffffffcccffffcccccbccdddc666999ffb1fffb6666111fffff999ff1111111111ffff56777666eeee2222222e2ebb44eebbb22ee2222222ee222222222222
                        6999999966666ccccdddbbbbbbbcbbbccfffffcfcccffcffcccbbcbcccceeee99f1fb11fffbbbb111111fffff111111111111bff567776999eeb2222222e2eb11444eeeb222222222222e22222222222
                        6999999eeeee6cccdddbbbbbbbcbbbcccfcfcccfccfffcccfccbbbcdcceeeeee9f1bfb11ffffffbb11111f111111111111111bb6577769999ebb222222eebeb111144eeb22222e2222222e2222222222
                        999999eebbbeeccdddbbbbbbccbbbbcccccccccfccccfccccbcbbdccce222eeef11bffb11ff666ffbbbb1f11111111111111bb6557766999eeb2222222eebebb111144eeee2222ee222222e222222222
                        999999eebbbbeccdddbbbbdbcbbbbcccbcbbcccfffccfcccbbcbbdccee222eee11bfffbb111ff999ffffbffffffffffff11b665577766ff6ebb2222222eebebb1111144eeee22222ee22222222222222
                        999999eebb22eccdddddddcdbbbbeeeeeeeeccccffcccccbddcdddcee2222eee1bff99ffb1111f999999ffb11111111bfff65557776611ffeb22222222eebbbb111111444eee222222ee222222222222
                        99999eeeeb22ecccdddddcddbbbbebbbbeeeeccccccccccdddcddcce2222eeeeff99999ffb111f999999ffb111111111bb655777776111bfeb22222222eebbeb1111111444eee22222eee22222222222
                        999999eeeb222eccddddcddbbbbcebbb22eeeebccccccbccddccccce2222eeeef9999996ffbb11ff9999fffffff11111b65577777611bbbfeb22222222eebb2bb1111111444eee222222eeee22222222
                        999999eeebb22eeccccdddbbbbccebb2222eeeebbcbbbbcccccceee222ee444eee99999666fb1111f99ffb1111fff11b6557777776bbbbffeb22222222ebb22ee1111111144eeeeeee22e22eee222222
                        9999eeeeeebb22eccdddbbbbbcccceb2222eeeebbbccbbcbccee222222e444411e99666666fbb1111ff111111111fff6557776776ffbbf1feb22222222ebb22eb11111111eeeeeeeee222e2222222222
                        9999eeeeeebbb2eecdddddbbccccceb222eeeeeebbbccbdccee222222eeee4111ee66666669fffb111fffff1111111f6577777661bfbbf1febb2222222eb222eb111111eeeeeeeeeeee22ee222222222
                        999eeeeeeeeeb22eedddddccccccbcb2222eee2ebbbdbdddce22222ee444ee1111ee6666669999ffffffbbbffff1116577777761bbfff1bfeeb22222222b222eb111111eee344eeeeee222ee22222222
                        99eeee2222eeb222eddddcccccbbccb2222eee2edddddbddce2222ee4e415711111e6666669999ff11111111bbf116577777666bbfff11bfeeb22222222b222eb111111ee344eeeeeeee22ee22222222
                        99ee222222eeb222ecddccddbbbbcceb222eee2eeddddddd22222eeee44157e1111e6666669999f1111111111bff6557777666bbff111bbfeeb2222222eb222eb1111eee34411111eeee222e22222222
                        9ee2222222eeb222ecccccddbbbbcceb222ee222eeddddccce22ee44e115771e111e6666699999f1111111111bb67777776666bff111bbffeebb222222eb222eb1111eee34ee11111eeee222ee2e2222
                        9ee2222222eeb222ecccddddbbbccceb222ee2222edddcccce22ee441155766eeeee6666699999fff11111111b6557776666fbf1f1bbbff6eebb222222eb222ebb11eeee44ee11111e3ee2222e2e2222
                        eee2222222eeeb22eeccddddddccccebb2eee2222ecccccccee2e44e11577661e1e6666699999921f111111bf6557776661bffffbbbfff66eeebb22222ee2222eb111ee34eee11111eeee2222e2e2222
                        ee22222222eeeb222eccdddddcccccebb22ee2222eccbccccee2eeeee5577611eee66666999999fbf11111bf555776666bbbf11ffff66666eeebbb2222ee2222eb11ee334eeee11eeeeeee222e2e2222
                        ee222222222eee222eecddddccccccee222ee2222ecccbcccee2eee11577761eee66666669999ffbffbfbff655766666fbbff11bff666666eeeebbbbb2eee222eb11ee3444eeeeeeeeeeeee22e2e2222
                        e222222222222e222eeecdcccbbbbcce22eee222eecccbddceeeeee11577761eee6666666999f1ff21fff665577666fffffbbbbff66666666eeeeeeeebeee222eb111e3444ee4444eeeeeee222ee2222
                        e222222222222ee222eecccddbbbbcce22ee4222eccccccdcceeee1e157776ffeee66666699f11bfbbfb265577666bf111fbfff66666666666666666eee2ee222e11ee3444ee44444eeeeee222ee2222
                        e222222222222eee222eeccdddbbbcce22e44222eccccbcccce2ee11577776ffeee666666ff11bfffff66557769fbf111ffff6666669996666555556666eee222e11ee3444eee4444eeeeee222ee2222
                        22222222222222eee222eccddddddcce2ee42222ecccccbcceeeeee1577776fffeee6666f111bbfff16557776bbfff1bfff66666999966655555555557666eee2e111e3444eee444eeeeeee222ee2222
                        222222222222222eee22eecdddddccceee42222eecccccbbce2ee115777776fffeeee66f11bbbbfff6757777fbbff1bfff66666966666665555555555555666e2e111ee3444eeeeeeeeeeee222ee2222
                        2222222222222222eee22ecddddcccceee42222ecccbbccbce2e1115777776fffeeee6f11bbbffff67557776fbfbbbff6666666666666666665557755555566eeeee1eee4444eeeeeeeeeee222ee2222
                        2222222eeeeeee22eeee2eecddcccceee42222eecccbbcccce2ee155777776ffffeeef11bbff9fff67577776fffbfff666666555555555666665577775555556ebeee1eee44444eeeee4eee222ee2222
                        222222eeeee222222eeee2eeccccceeee22222eccccbbbccce2eee57777766ffffeef11bfff99ff675577776fbff666667555555555555576666557777755556eb2e211ee444444ee444eee222e22222
                        22222eeeee22222222eeeeeecccceee2222222eccccdbbccee2eee57777766ffffef11bbf9999f6675777776fbf66666555555555555777555665577777755556bb22211eee44444444eeee222e22222
                        2222eeeeee22222ee22eeeeeeeeeeee2222222ecccbdbbcce22eee57777766fffff11bbf99999f6665777777ff6666675557655557666677755765557777775576b222e11ee444ee4eeeeee222e22222
                        222ee222ee222222eeeeeeeeeeeeee2222222ecbccbdbbcce22eee57777766ffff11bbff99999f6995577777666666655555555555777766777766556777777556eb2ee111eeeeeeeee44ee222e22222
                        22ee2222ee222222eeeeeeeee22ee2222222eecdcccdbbcce22eee57777766fff11bbfeeee999669965557777766665555555555555557777777766776777777566bb2eee1111eeee1144eee22e22222
                        2ee22222eee2222222eeeeeeeee222222222eecdcccddbccee2ee557777766ff11bbfee1eee99699965557777776655555555777777757777777766777677777776ebb2eeeee111111114eee22e22222
                        2ee22222eeee222222222222eeeeeee22222ecddcccddbccceeee557777766f11bbffe1111eeeee9996557777777765557777777777777777777776677767777776eebb22eeeeeb111114eee22e22222
                        2ee22222eeeeeeeeee222222222222222222eccdbbcddbbcceeee5577777666bbfeeeee1111eeee9996757777777776557777777777777777677776667767777776eeeb2222eeeebb11144ee2ee22222
                        2ee22222eeeeeeeeeeeeeee2222222222222ecccddcbdbbccceee55777777666bf111ee111eeeeee666655777777777655577777777777777767777667777777776eeebbb2222eeebbb114e22ee22222
                        2e222222eee44eeeeeeeeeee22222222222eecccbdbcddbccceee55577777766fe1111ee14eee22e6666657677777777765577677777777777677776677777777766eeeeeb2222eeeebbb4e22ee22222
                        2e2222222e1e1ee4eeeeeeeee2222222222ecccccddbddbbcceee55577777776ee1111ee1eee222e66666756777777777766777667777777776777766667777777666eebebbbbbee2eeeebe2eee22222
                        2e2222222e1eee1e4eeeeeeeee22222222eeccccccdbdddbcccee55577777776eee1114eeee2222e66666677666777777777677766777777776777766667777777666eeeeeeeeb2222e22ee2eee22222
                        2e2222e22e11e111e1e44eeeeeee222222eccbbcccddbbddbccee5557777777656e1114eee22222e6666666777767777777776677767777777677777666777777766eebbe2eeeee2222e22e2eee22222
                        222222e22eeee11ee1114e4eeeeeeeeeeeecdbbbbccddbddbcceee557777777756ee444eee22222e5555566677776677777777767776777777677777667777777776eebb22222ee22222e2e2eee22222
                        222222eb2e111eee1111ee14eeeeeeeeeeccdbbbbbbbdcddbbccc55557777766566644eee22226555555556966777767777777776677677777777777667776777776eebb222222e22222e2222e22e222
                        222222eb2ee11eeee11e111ee4eeeeecccccdbbbbbbbbbcdbbccc65557777766566566e2666666655555555655677777777777777767767777777777667776777776eebb222222ee222eeeeeeeeee222
                        222222eb22e1ee1e1eee11e1114eeccdbcccddddddbbbbbdddbcccc55777776756655666665555565777775655567777777777777767766777777777667776777776eebb2222222ee22eeee222222222
                        222222eb22eee11eeeeeee1111eecccdbccccdddddddbbbcdddbccc65777767776575655565555565777777677766557777777777776776777767777666776777776eebb2222222ee22eeeee22222222
                        222222eb222e111111eee1111ccccccdbcccccccccdddbbbcbddcccc6777767767775655556777567777777677777665577777777777676777767777666776777776eebb22222222e22ee22eee222222
                        222222eb222ee11111eee111cccbcccdbbcbcbbbcccdddbbccddddccc677777677777655757677776777777677777776555777777777676677767777666776777776eebb22222222222e222eee222222
                        222222eb2222ee1111e1eeeecccbcccddbccccbbbbcddddbbccdddccccc77676777776777776777767777776777777776755776777776766777677766667767777766ebbb222222222222222ee222222
                        222222eb2222eee11ee111ecccccbbcdddbbccbbbbcccddbbccccdbccccc6667777776777776777767777776777777776665776777776776777677777667677777766ebbbb2222222222222222222222
                        222222ebb222eeee1e111ccccbccbbbdddbbbbcbbbbccdddbbccccbbbbbccc77777666777776777767777776777777776665577677776776677677777667677777766eebbb222222222eeee222222222
                        222222eeeb222eeeee1ccccddbccbbbcddddbbbccbbbccddbbbcccccbbbccc77766667777776777767777776677777777666577677777776677777777677777777666beebbbbbbee2eeee22222222222
                        222222eeeebb22eee1cccccddbbbcbccccddbbbbcccbbccddbbbbcccccbbcc66666777777767777667777776677777776666777677777776666777776667777776666bbbeeebbeee2222222222222222
                        222222eeeeebb222eecccccdddbbccbccccdddbbbbbccccddbbbbbbccccbb666667777777767777667777766777777766666677677776776667777777667777776666bcbbeeeee222222222222222222
                        2222222eeeeebbb2cccbbcccdddbbcccccccddbbbbbbbcccddbbbbbbccccbb6777777777767777767777776777777766666667766777666666677766666667776666bbccbee222222222222222222222
                        222222222eeeeeeeccbbbbcbcddddbcccccccddccbbbbbccddbbbbbcccccbb6677777776777676667777666777777666bb666667777766666bb6666bbbbb666666bbccccbbeeeeee22222222222eeeee
                        22222222222eeeeeccbbcccccccddddbbccbbccccbbbbbccddbbbbbccccccbb6666666666666666777666b66666666bbbbbb6666666666bbbbbbbbbbcccbbbbbbbbbcccccccbbeeeeeeeeeeeeeeeebbb
                        ccc2ccc22222eeeeccbccccccccccddbbbbbcccccccccccddbbbbcccccccbbbbb66666bb66666bb6666bbbbbbbbbbbbcccbbb6666666bbbccccccccccccccbbccccccccccccccbbbbbbbbbbbbbbbbbcc
                        ccccccccc22222222cccccccccccccccccbcccccccccccbbbbbbcccccccbbbcbbbbbbbbbbbbbbbbbbbbbccccccbbccccccccbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccccccc
                        ccccccccccccc222ccccccccccccccccccccccccccccbbbbbbcbbbbbbbbbccbbcccccccccccccccccccccbccbbccccccccccccccccccccccccccccccccccccccccccccbccccccccccccccccccccccccc
                        ccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbcbbbbccccccbbccccccccbbbcccccccbbcccccbbcccccccccccccccccccccccccccccccccccccccccbbccccccccccccccccccccccccc
                        ccbbbbccbbbccccccccccccccccccccccccccccccccccbbbcccccccccccccccccbbbbbbbbbcbbbbbbbcccccccccbbbbccccccccccccccccccccccccccbbbcccccccbbbccccccccbccccccccccccccccc
                        cccccccbbbbbbcbbbbbbcccccccccccccccbbbbbbbcccccccccccccccccbccccbbbbbcccccccccbbbcccccccccccccbbccccccccccccccccccccccbbbbbcbcccbbbbcccccccccccbcccccccccccccccc
                        cccbcccccccccbbbbbbbcccccccccccbbbbcbbbbcccccccccccccccccccbbbbbbbbccccccccccccbbccccccccccccccbbbbcccccccccccccccccbbbbbccccbbbbbccccccccccccbbbbbbbbbbcccccccc
                        cccbbbbbccccccccbccccccccbbbbbbbbbbbbbbbbcccccccccccccccccccbbbbbbccccccccccccbbbcccccccccccccccccccccccbbcccccbbbbbbbbbcccccccccccccccccccccccccbbbbbbbbbbccccc
                        ccccccccbbccccccbbbbbbbbbbbbccccccbbcccbbbccccccccccccccccbbbbbbbbbbbcccccbbbbbcbbbcccccccccccccccccccccccbbbbbbbbcccccccccccccccccccccccccccccccccccccccccbbbbb
                        cccccbbbbbccccccccccccccccccccccccccccccccbbbbbccccccccbbbbbccccccccccccccccccccccbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
                        ccccccccbccccccccccbbccccccccccccccccccccccbbccbbbbbccbbbccccccbbbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbcccccccccccbbbcccccbccccccccccc
                        cccccccccbbbbbcccccccbbccccccccccccccccccccccccccccccccccccccbbcccccccccccbbbcccccccccccccbccccccccccccccccccccccccccccccccccccbcccccccccbbbcccccccccbbbbbbbbccc
                        ccccccccccccccbbbbbbbbbcccccccccccccccccccccccccccccccccccccbbccccccccccccbccbbbcccccccccccbbcccccccccccccccccccccccccccbbbbbbbcccccccccbccccccccccccccccccbbbbb
                        bbbbbbbbbcccccbbbbbbbbbbbbccccccccccccccbbbbbbbbccccccccccbbbccccccccccccccbbbbbbbbcccccccccbbbccccccccccccccbbbbbbbbbbbbccccccccccbbbbbbccccccccccccccccccbbbbc
                        ccccccbbbbbbbbbbbbbcccccccccccccccccccccccccccccbbbbbbbbbbccccccccccccccccbbbbbbbbbbbcccccccccbbbbbbbbbbccbbbbbbbccbbcccccccccccccccccccccccccccccccccbbbbbbbbbb
                        cccccccccccccbbbbbbbbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbbbbbbccccccccccccccbbbbbbbbcccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbb
                        cccccccccccccccccccccbbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbccccccccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbc
        """))
        mySprite.set_position(0, 96)
        mySprite.set_position(3, 96)
        mySprite.destroy()
        game.show_long_text("莫莉(本篇主角)", DialogLayout.BOTTOM)
        game.show_long_text("緩慢地走進傳送門", DialogLayout.BOTTOM)
        game.show_long_text("等待他的是一堆奇異的植物", DialogLayout.BOTTOM)
        game.show_long_text("有的還長滿眼睛直視著她", DialogLayout.BOTTOM)
        p1 = sprites.create(img("""
                ................................................
                            ...................fffffffffff..................
                            ..................fbbbbbbbbbbff.................
                            ..................fbbbcbccbcbbf.................
                            .................ffbbbbbbbbbffffffff............
                            .................fbbbbbbbcffbbbbbbbffff.........
                            .................fcbbbbbcfbbccccccccbbf.........
                            .................fccccccfbcccccccccccff.........
                            ..............ff6ffffffffffffffffffff...........
                            .............ff9ffefbbbffffbbfffff..............
                            .............f49fefdddd1ffddd1ffdf..............
                            .............f49ffffddd1ffddd1ffdf..............
                            .............f4496ffdddd33ddddd3ff..............
                            .............f44eefffdddddfddfddf...............
                            ........ff.ff44eeeefffddddfffddff...............
                            ........ffff44eeeeeeffffddddbfff................
                            .........ffffeeeeeeffffffddbf...................
                            ............ffeefffffff6ffdbffffff..............
                            .............ffffff44f966ffff6ff44ff............
                            ...............ffff455f6999ff669f4fff...........
                            ..............ff999f555f699fff966ff9f...........
                            ............ff999999f55f66669ff969fff...........
                            ...........ff9999966f44f9669999f999fff..........
                            ..........f999966666f44f99999f9f999f6ff.........
                            ..........f9996666fff44f9999999f966f99ff........
                            ..........f99966ffeffef999999f9f66ff6999f.......
                            ..........f9996ffeeeff669996669f6f.ff699f.......
                            ..........f99999fffefff666666fffff..ff699f......
                            ..........ff666999fefffffffffffccf.ff6999ff.....
                            ...........ff66669ffffffccccccccbf.f666999f.....
                            ............ff66fffdffccccccccccbfff66699ff.....
                            .............ffffdddfffccccccccbbfff6699ff......
                            ...............fddddffccccccccbbbffd669ff.......
                            ............ffffdddbffffffffffffffbdffff........
                            ............fdddddbfcfccbbbbbbbfffbddf..........
                            ............ffbbbbffcbcbbbbbbbbbbbfbddf.........
                            .............ffffffcbccbbbbbbbbbbbffbbf.........
                            ..............fffffcbcbbbbbbbbbbbbbffff.........
                            ................fccbccbbbbbbbbbbbbbfff..........
                            ................fcccccbbbbbbbbbbbbbbbf..........
                            ................fcccbbbbbbbffffbbbbbbbf.........
                            ................fccbbbbbbbbfffcbbbbbbbbf........
                            ................fccbbbbbbbbffccbbbbbbbbff.......
                            ................fcbbbbbbbbbfffccbbbbbbbbf.......
                            ................fbbbbbbbbbbf.ffcbbbbbbbbf.......
                            ................fbbbbbbbbbff..fccbbbbbbbbf......
                            ...............ffbbbbbbbbff...ffccbbbbbbbf......
                            ...............fbbbbbbbbff.....ffcbbbbbbbbf.....
            """),
            SpriteKind.player)
        p1.set_position(16, 64)
        game.show_long_text("莫莉：酷ㄟ!這什麼地方啊?", DialogLayout.BOTTOM)
        game.show_long_text("據說每個地方都有守護者", DialogLayout.BOTTOM)
        game.show_long_text("守護者身上都有者碎片", DialogLayout.BOTTOM)
        game.show_long_text("只有...啊啊啊!有怪物!", DialogLayout.BOTTOM)
        p1.destroy()
        p1 = sprites.create(img("""
                ................................................
                            ...................fffffffffff..................
                            ..................fbbbbbbbbbbff.................
                            ..................fbbbcbccbcbbf.................
                            .................ffbbbbbbbbbffffffff............
                            .................fbbbbbbbcffbbbbbbbffff...f.....
                            .................fcbbbbbcfbbccccccccbbf...ff....
                            .................fccccccfbcccccccccccff..f1ff...
                            ..............ff6ffffffffffffffffffff....f11f...
                            .............ff9ffefbbbffffbbfffff......ff15f...
                            .............f49fefdddd1ffddd1ffdf......f15ff...
                            .............f49ffffddd1ffddd1ffdf......f15f....
                            .............f4496ffdddd33ddddd3ff.....ff15f....
                            .............f44eefffdddddfffdddf......f15ff....
                            ........ff.ff44eeeefffddddffdddff.....ff15f.....
                            ........ffff44eeeeeeffffddddbfff......f155f.....
                            .........ffffeeeeeeffffffddbf.........f155f.....
                            ............ffeefffffff6ffdbffffff...ff55ff.....
                            .............ffffff44f966ffff6ff44ff.f155f......
                            ................fff455f6999ff669f4ffff15ff......
                            ...............ff99f555f699fff966ff9ff55f.......
                            ...............f9999f55f66669ff969fff15ff.......
                            ...............f9999f44f9669999f999ff55f........
                            ...............f9999ff4f99999f9f999f15ff........
                            ...............ff9996fff9999999f96ff15f.........
                            ................f699996f99999f9f6fff5ff.........
                            ................ff999996f996669f6f155f..........
                            .................f6999999f666fff9f155f..........
                            .................ff699996ffff999f155ff..........
                            ..................ff6996999ff999f155ff..........
                            ...................ff6999999f99ff15f6f..........
                            ....................fff99999ffff155f6f..........
                            ...................fffff999ffffff5ff6f..........
                            ...................ffccff9ffddfffff6f...........
                            ...................fccccfffddddfffff............
                            ..................ffcbccffdddddddfbf............
                            ..................fcbccbffddddddffbf............
                            .................ffcbcbbbffbddbffbbf............
                            ................fccbccbbbbffbbffbbbbff..........
                            ................fcccccbbbbbfffbbbbbbbf..........
                            ................fcccbbbbbbbfffbbbbbbbbf.........
                            ................fccbbbbbbbbffcbbbbbbbbbf........
                            ................fccbbbbbbbbffccbbbbbbbbff.......
                            ...............ffcbbbbbbbbbfffccbbbbbbbbf.......
                            ...............ffbbbbbbbbbbf.ffcbbbbbbbbf.......
                            ..............fffbbbbbbbbbff..fccbbbbbbbbf......
                            ..............fffbbbbbbbbff...ffccbbbbbbbf......
                            ..............ffbbbbbbbbff.....ffcbbbbbbbbf.....
            """),
            SpriteKind.player)
        p1.set_position(16, 64)
        game.show_long_text("磷化氫(很像氣體", DialogLayout.BOTTOM)
        game.show_long_text("會順移但...", DialogLayout.BOTTOM)
        game.show_long_text("每24小時只能一次)", DialogLayout.BOTTOM)
        scene.set_background_image(img("""
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        """))
        game.show_long_text("茉莉:...發身什麼事!?", DialogLayout.BOTTOM)
        game.show_long_text("系統已上線", DialogLayout.BOTTOM)
        game.show_long_text("系統:只要遇到外星人", DialogLayout.BOTTOM)
        game.show_long_text("就...變白..", DialogLayout.BOTTOM)
        game.show_long_text("自...小..心", DialogLayout.BOTTOM)
        game.show_long_text("系統已下線", DialogLayout.BOTTOM)
        mySprite2 = sprites.create(img("""
                ................................................
                            ................................................
                            ................................................
                            ................................88888888........
                            .....................8888888...88999988.........
                            ..................88899999988.88919688..........
                            .....88888.......89999999999888911988...........
                            ....8899988.....89999999999198999968............
                            ...888889188...889999899999198899968............
                            ...8...891188..899998869999119899688............
                            ...8....8919888899888b8699991189968.............
                            ........8699998998d2db8669999998688.............
                            ........86998999682d2db88699919868..............
                            ........86988996688ddddb8869999888....8.........
                            ........866899666888ddddb86699988.....8.........
                            ........868898888668888db88699998....88.........
                            ........888988dd88888888888669998888888.........
                            ........88998ddd8999699968886999999998..........
                            .......8899688888996999996886666686888..........
                            .......899688bc869969999968886888898............
                            ......889668bd88669969999689888dd898............
                            .....8896888d8888666666668898bddd8988.....8.....
                            ...889968898d898888888888899888888998....888....
                            ....88888898866888888888889988bc869988..8898....
                            .........898696898888888889998d8869998889988....
                            .........896696898888888886998d886999999988.....
                            ...8.....896968988999999986698868669999998......
                            ...88...8899688889999999988698868666999668......
                            ...8888.8999889899199999998898668886666688......
                            ...89988889689689119999999989869988888888.......
                            ...8899118989688919999999998986998..............
                            ....869918989689119999999988986998..............
                            ....866998889689119999999988999668..............
                            ....886698899689911999999888996688..............
                            .....8866996668669199999988896688...............
                            ......8886668888669999999898688.................
                            ........8888...88669999998988...................
                            ................886999998998....................
                            .................86669998998....................
                            ..................886998888.....................
                            ...................8668888......................
                            ....................8688........................
                            ....................888.........................
                            ...................888..........................
                            ..................8888..........................
                            ..................88............................
                            ................................................
                            ................................................
            """),
            SpriteKind.E1)
        mySprite2.set_position(146, 64)
        game.show_long_text("磷化氫:你..說誰是怪物?", DialogLayout.BOTTOM)
        game.show_long_text("豈有此理!膽敢踏入此地", DialogLayout.BOTTOM)
        game.show_long_text("還說我是怪物!!", DialogLayout.BOTTOM)
        game.show_long_text("別想活著回去！", DialogLayout.BOTTOM)
        game.show_long_text("戰鬥  開始", DialogLayout.CENTER)
        game.show_long_text("解說:此為回合篇選擇制戰鬥", DialogLayout.BOTTOM)
        game.show_long_text("主角絕對不會死", DialogLayout.BOTTOM)
        game.show_long_text("選擇以下兩種武器", DialogLayout.BOTTOM)
        game.show_long_text("武器可能與劇情無關", DialogLayout.BOTTOM)
        game.show_long_text("請勿大驚小怪", DialogLayout.BOTTOM)
        game.show_long_text("能克制外星人則直接死亡", DialogLayout.BOTTOM)
        game.show_long_text("無則無法造成傷害", DialogLayout.BOTTOM)
        game.show_long_text("選擇出現", DialogLayout.BOTTOM)
        game.show_long_text("請只選擇a或b", DialogLayout.BOTTOM)
        game.show_long_text("謝謝配合", DialogLayout.BOTTOM)
        game.show_long_text("解說完畢", DialogLayout.BOTTOM)
        game.splash("請選擇攻擊武器")
        mySprite.say(game.ask("a螢光劍 b弓箭"))
        if controller.A.is_pressed():
            game.show_long_text("磷化氫使用衝擊", DialogLayout.BOTTOM)
            game.show_long_text("茉莉被撞倒", DialogLayout.BOTTOM)
            game.show_long_text("茉莉使用香蕉皮", DialogLayout.BOTTOM)
            game.show_long_text("磷化氫無效", DialogLayout.BOTTOM)
            game.show_long_text("磷化氫使用雷射光", DialogLayout.BOTTOM)
            game.show_long_text("手滑照到自己", DialogLayout.BOTTOM)
            game.show_long_text("茉莉受傷", DialogLayout.BOTTOM)
            game.show_long_text("磷化氫使用大招", DialogLayout.BOTTOM)
            game.show_long_text("(死亡雷射光)", DialogLayout.BOTTOM)
            game.show_long_text("茉莉使用螢光劍", DialogLayout.BOTTOM)
            game.show_long_text("反射力量", DialogLayout.BOTTOM)
            game.show_long_text("磷化氫死亡", DialogLayout.BOTTOM)
            game.show_long_text("磷化氫可..可惡..啊", DialogLayout.BOTTOM)
            game.show_long_text("獲得碎片", DialogLayout.BOTTOM)
            mySprite2.destroy()
        else:
            game.show_long_text("根本不痛不癢", DialogLayout.BOTTOM)
            game.show_long_text("你已死亡", DialogLayout.BOTTOM)
            game.show_long_text("請重新遊玩", DialogLayout.BOTTOM)
            game.reset()
game.on_update(on_on_update)

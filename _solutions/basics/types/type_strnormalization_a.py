
a = A.upper().replace('UL', '').strip().title().replace('Iii', 'III')
b = B.upper().replace('UL.', '').strip().title().replace('Trzeciego', 'III')
c = C.upper().replace('ULICA', '').strip().title().replace('Iii', 'III')
d = D.upper().replace('\n', '').strip().title().replace('3', 'III')
e = E.upper().replace('UL.', '').strip().title().replace('Iii', 'III')
f = F.upper().replace('ULICA', '').strip().title().replace('Iii', 'III')
g = G.upper().replace('ULICA.', '').strip().title().replace('Iii', 'III')
h = H.upper().replace('3', 'III').strip().title().replace('Iii', 'III')
i = I.upper().replace('\t', ' ').strip().title().replace('Iii', 'III')

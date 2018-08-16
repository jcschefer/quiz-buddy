# Inserts data for the NSC PACE tournament 2018
# run this script from the web directory's base directory

from data.models import Tournament, Packet, Question, PacketType
from .idempotents import get_or_create_tournament, get_or_create_packet, get_or_create_question

# 1. insert the tournament
tournament = get_or_create_tournament(Tournament(name='PACE NSC', year=2018))

# 2. Packet for round one
round_1 = get_or_create_packet(Packet(tournament=tournament,
                                      name='Round 01', round_number=1, packet_type=PacketType.TOSSUP.name))

r1_q1_t1 = 'It is implied that these figures created "The Diary of P." and "The A.B. Memoires," as well as objects found in a footlocker near Bangor. These figures often greet and say goodbye to each other with the phrase "Under His Eye." One of these figures finds the phrase "nolite te bastardes carborundorum" carved into a cupboard. Groups of these figures use their bare hands to kill a condemned person in a type of salvaging known as a'
r1_q1_t2 = 'Paricicution. These figures are trained by Aunts at Rachel and Leah Centers, and are given new names referring to the member of the ruling class of Gilead to whom they are assigned. The protagonist Offred is a member of,'
r1_q1_t3 = 'for 10 points, what group of fertile women in a novel by Margaret Atwood'
r1_q1_answer = 'handmaids'
r1_q1 = get_or_create_question(Question(packet=round_1, text_part_1=r1_q1_t1,
                                        text_part_2=r1_q1_t2, text_part_3=r1_q1_t3, answer=r1_q1_answer, number=1))

r1_q2_t1 = 'The Czech engraver Wenceslaus Hollar made panoramic engravings before and after this event. This event is commemorated by a 202-foot-tall monument topped by a golden urn that, until 1830, had an inscription blaming it on the "malice of the Popish faction"; that monument was co-designed by Robert Hooke, who was appointed surveyor after this event. Charles II was informed of this event by a man who wrote of burying his cheeses during it,'
r1_q2_t2 = 'Samuel Pepys. The Duke of York commanded troops that tore down buildings during this event. This event ended on Pie Corner, leading some to attribute it to God\'s wrath at the sin of gluttony, and supposedly began at a bakery on Pudding Lane.'
r1_q2_t3 = 'For 10 points, name this 1666 conflagration in England\'s capital.'
r1_q2_answer = 'Greate Fire of London'
r1_q2 = get_or_create_question(Question(packet=round_1, text_part_1=r1_q2_t1,
                                        text_part_2=r1_q2_t2, text_part_3=r1_q2_t3, answer=r1_q2_answer, number=2))

r1_q3_t1 = 'A theorem introduced by this man gives a formula to find the radii of four mutually tangent circles. The second book of a work by this mathematician consists of a classification of algebraic curves, including his namesake "folium." This man is the inventor, and sometimes the namesake, of the field of analytic geometry.'
r1_q3_t2 = 'This man\'s three "laws of nature" were a major influence on Isaac Newton\'s laws of motion. An upper limit on the number of positive roots of a polynomial can be found using this mathematician\'s "rule of signs." In two dimensions, ordered pairs are used to represent the x and y coordinates of numbers in his namesake coordinate system.'
r1_q3_t3 = 'For 10 points, name this French mathematician, who, in a famous work of philosophy, stated "Cogito ergo sum."'
r1_q3_answer = 'Rene Descartes'
r1_q3 = get_or_create_question(Question(packet=round_1, text_part_1=r1_q3_t1,
                                        text_part_2=r1_q3_t2, text_part_3=r1_q3_t3, answer=r1_q3_answer, number=3))

r1_q4_t1 = 'A narrative about two of these objects and a hidden marble are used in a psychological experiment devised by Simon Baron-Cohen to assess whether children attribute false beliefs to others. Papers published in 1939 and 1940 described experiments in which subjects were asked to choose between two of these objects with different characteristics by researchers Kenneth and'
r1_q4_t2 = 'Mamie Clark. These objects, which are central to the "Sally-Anne task," were used in research summarized by expert witnesses in the Brown v. Board case. Social learning theory was devised based on an experiment in which children imitated adults\' actions toward one of these objects.'
r1_q4_t3 = 'For 10 points, what kind of object did adults beat up in Albert Bandura\'s experiment involving a "bobo" one?'
r1_q4_answer = 'dolls'
r1_q4 = get_or_create_question(Question(packet=round_1, text_part_1=r1_q4_t1,
                                        text_part_2=r1_q4_t2, text_part_3=r1_q4_t3, answer=r1_q4_answer, number=4))

r1_q5_t1 = 'In this opera, a soft timpani roll underlies a shift from B-flat major to the mediant of G major during the sextet "Sola, sola in buio loco." This opera\'s final sextet, "Questo è il fin di chi fa mal," which delivers the moral, was cut in most 19th-century productions. At a dinner scene in this opera, a character claims to be sick of constantly hearing the composer''s earlier "Non più andrai." In this opera\'s aria "Il mio tesoro," Don'
r1_q5_t2 = 'Ottavio swears to avenge the murder of Donna Anna\'s father. Its title character woos Masetto\'s betrothed Zerlina in the aria "Là ci darem la mano," and Leporello recounts its title character\'s sexual conquests in the "Catalogue Aria."'
r1_q5_t3 = 'For 10 points, name this Mozart opera that ends with a statue of the commendatore dragging the title seducer to hell.'
r1_q5_answer = 'Don Giovanni'
r1_q5 = get_or_create_question(Question(packet=round_1, text_part_1=r1_q5_t1,
                                        text_part_2=r1_q5_t2, text_part_3=r1_q5_t3, answer=r1_q5_answer, number=5))

r1_q6_t1 = 'This deity becomes enraged when she is reminded of a man who brought her dates but refused to sleep with her, after which she turned him into a mole. A partially-extant poem describes this deity turning a bandit woman into a waterskin. The gala-tura and the kur-jara rescue this deity after a journey in which she is repeatedly delayed by the gatekeeper Neti. This deity, who was attended by Ninshubur, was cursed with'
r1_q6_t2 = 'sixty diseases by Namtar. The Bull of Heaven was sent after Enkidu and Gilgamesh by this goddess, who removed one item of clothing at each of seven gates when descending to the underworld, which was ruled by her sister Ereshkigal.'
r1_q6_t3 = 'For 10 points, name this wife of Dumuzid or Tammuz, the Mesopotamian goddess of love and sex.'
r1_q6_answer = 'Ishtar, Inanna, Astarte'
r1_q6 = get_or_create_question(Question(packet=round_1, text_part_1=r1_q6_t1,
                                        text_part_2=r1_q6_t2, text_part_3=r1_q6_t3, answer=r1_q6_answer, number=6))

r1_q7_t1 = 'The existence of these things was accidentally revealed by Alexander Butterfield. Some of these things were stored at a facility in Yorba Linda, California, and not released to the public until 2013. One rejected compromise involved making Senator John C. Stennis the only person allowed to review these things. Political cartoonists made fun of the so-called "Rose Mary'
r1_q7_t2 = 'Stretch," an awkward posture supposedly used to accidentally destroy parts of one of these things. That stretch resulted in an 18-and-a-half minute gap in them. The Saturday Night Massacre followed Archibald Cox\'s insistence on receiving these secretly-made objects.'
r1_q7_t3 = 'For 10 points, name these audio records of a president who resigned during the Watergate scandal.'
r1_q7_answer = 'Nixon Tapes'
r1_q7 = get_or_create_question(Question(packet=round_1, text_part_1=r1_q7_t1,
                                        text_part_2=r1_q7_t2, text_part_3=r1_q7_t3, answer=r1_q7_answer, number=7))

r1_q8_t1 = 'A book by this author ends with the Wandering Jew informing the narrator that a door in his museum was made from the gate of ivory that Aeneas once passed through in Hades. That book by this writer ends with the story "The Virtuoso\'s Collection," and it includes a story in which Annie opens an ebony box and her infant child crushes Owen Warland\'s mechanical butterfly. Another of his stories ends by noting that "no hopeful verse" was carved on the'
r1_q8_t2 = 'tombstone of the title character\'s grave. This author included "The Artist of the Beautiful" in a collection named for his home, Mosses from an Old Manse, which also features a story set in Salem where the title character sees a procession in a forest.'
r1_q8_t3 = 'For 10 points, name this author of "Young Goodman Brown."'
r1_q8_answer = 'Nathaniel Hawthorne'
r1_q8 = get_or_create_question(Question(packet=round_1, text_part_1=r1_q8_t1,
                                        text_part_2=r1_q8_t2, text_part_3=r1_q8_t3, answer=r1_q8_answer, number=8))

r1_q9_t1 = 'A recent restoration of this painting revealed two spiderwebs behind the two donors in it and proved that the wood used for the hermit panel was the same as its others. This painting was rescued from an Austrian salt mine shortly before the mine was blown up by the Nazis. Equestrian portraits of men such as Philip the Good are included in a panel of this painting called "The'
r1_q9_t2 = 'Just Judges" that was stolen in 1934. The man who completed this painting called himself "second in art" to his deceased brother. When closed, this work shows grisaille statues of saints below an Annunciation scene. When opened, it reveals a panel of a large procession gathering around a lamb about to be sacrificed.'
r1_q9_t3 = 'For 10 points, name this master altarpiece of Jan Van Eyck.'
r1_q9_answer = 'Ghent Altarpiece'
r1_q9 = get_or_create_question(Question(packet=round_1, text_part_1=r1_q9_t1,
                                        text_part_2=r1_q9_t2, text_part_3=r1_q9_t3, answer=r1_q9_answer, number=9))

r1_q10_t1 = 'Lev Landau showed that, under certain conditions, the cyclotron motions of charged particles have this property, a fact which allows resistance to be written in terms of the von Klitzing constant. A sharp peak at 254 nanometers corresponding to 4.9 electron-volts implied this result in an experiment that fired electrons through a vapor of mercury and was run by Franck and Hertz. When deriving his law of blackbody radiation,'
r1_q10_t2 = 'Max Planck arbitrarily assumed that energy has this property. Einstein explained the photoelectric effect by proposing that light is a particle, and thus has this property.'
r1_q10_t3 = 'For 10 points, name this property where at small scales, quantities become discretized, which names a subfield of physics involving wavefunctions and randomness.'
r1_q10_answer = 'quantization'
r1_q10 = get_or_create_question(Question(packet=round_1, text_part_1=r1_q10_t1,
                                         text_part_2=r1_q10_t2, text_part_3=r1_q10_t3, answer=r1_q10_answer, number=10))

r1_q11_t1 = 'One paper about this concept concludes by identifying the writer\'s position with Hegel, who saw this concept as a "distorted reflexion" of reality that Kant referred to this concept as a "form of inner sense" in the Transcendental Aesthetic. The A-series and B-series theories of this concept were introduced in a J. M. E. McTaggart paper titled for the "unreality" of this concept. Henri Bergson paired this concept with "free will" in the title of a book that uses the term'
r1_q11_t2 = '"duration." Theories of this concept include the "growing block," as well as a theory that holds that John F. Kennedy still exists.'
r1_q11_t3 = 'For 10 points, name this concept, subject of theories like presentism, that Einstein united into a manifold with space.'
r1_q11_answer = 'time'
r1_q11 = get_or_create_question(Question(packet=round_1, text_part_1=r1_q11_t1,
                                         text_part_2=r1_q11_t2, text_part_3=r1_q11_t3, answer=r1_q11_answer, number=11))

r1_q12_t1 = '30,000 people were killed in a raid orchestrated by this monarch against a city that had recently been captured by Hayreddin Barbarossa. His ineffective New Laws prompted the Valladolid  debates. The enormous fleet for this monarch\'s conquest of Tunis was mostly financed with the gold ransom delivered from Atahualpa. Troops fighting against the League of Cognac for this son of Philip the Handsome and Juana the'
r1_q12_t2 = 'Mad pillaged monasteries while sacking Rome. This king spent his gouty final years at a monastery after abdicating. His massive inheritance included the Habsburg Netherlands.'
r1_q12_t3 = 'For 10 points, name this Holy Roman Emperor and King of Spain who abdicated in 1556 in favor of his son, Philip II.'
r1_q12_answer = 'Charles V'
r1_q12 = get_or_create_question(Question(packet=round_1, text_part_1=r1_q12_t1,
                                         text_part_2=r1_q12_t2, text_part_3=r1_q12_t3, answer=r1_q12_answer, number=12))

r1_q13_t1 = 'In the Goldschmidt classification, species are grouped by whether their preferred host is rock, ores, gas, or this element. This element and a more dense one "rained out" of molten material during the "catastrophe" named for it, a key step in planetary differentiation. Siderophiles are named for their preference for this element, which is said to be'
r1_q13_t2 = '"telluric" if it is found on Earth as not part of an ore. This element bonded to sulfur forms galena. Ores of this element include a specimen historically called lodestone and the reddish-brown hematite. Fool\'s gold, or pyrite, is an ore of this metal, which along with nickel is a major element of the Earth\'s core'
r1_q13_t3 = 'For 10 points, name this magnetic chemical element abbreviated Fe.'
r1_q13_answer = 'iron'
r1_q13 = get_or_create_question(Question(packet=round_1, text_part_1=r1_q13_t1,
                                         text_part_2=r1_q13_t2, text_part_3=r1_q13_t3, answer=r1_q13_answer, number=13))

r1_q14_t1 = 'This author appended his essay "On the Use of the Chorus in Tragedy" to a play in which Don Manuel and Don Caesar are the title character\'s feuding sons. The villain of another of his plays is killed when a peasant woman named Armgart and her children delay him by pleading for clemency in front of his horses. Another of his protagonists is torn between honoring the sacrifices of Roller and Schweizer and his love for Amalia von Edelreich after being banished from his home by his father, the Count. This author of'
r1_q14_t2 = '"The Bride of Messina" wrote about the conflict between the brothers Franz and Karl Moor in one play, and another of his plays is titled for a huntsman who defies the Swiss tyrant Gessler.'
r1_q14_t3 = 'For 10 points, name this German playwright of "The Robbers" and "William Tell"'
r1_q14_answer = 'Schiller'
r1_q14 = get_or_create_question(Question(packet=round_1, text_part_1=r1_q14_t1,
                                         text_part_2=r1_q14_t2, text_part_3=r1_q14_t3, answer=r1_q14_answer, number=14))

r1_q15_t1 = 'In this country\'s capital, thousands of coins are nailed to a stump that supposedly cures toothaches. Eyes pointing in four directions are a motif on a monument at Swayambhunath in this country. A snake-infested floodplain that contains this country\'s capital was supposedly drained by the bodhisattva Manjushri, and many of its temples were built by the Newar people. The Terai Swamp in this country\'s south contributed to its'
r1_q15_t2 = 'isolation. This country became a republic in 2008 and was once ruled by the Ranas. It is home to the largest Sherpa population in the world. Its well-above-sea-level capital was devastated by a 2015 earthquake.'
r1_q15_t3 = 'For 10 points, name this mountainous Asian country with capital at Kathmandui.'
r1_q15_answer = 'Nepal'
r1_q15 = get_or_create_question(Question(packet=round_1, text_part_1=r1_q15_t1,
                                         text_part_2=r1_q15_t2, text_part_3=r1_q15_t3, answer=r1_q15_answer, number=15))

r1_q16_t1 = 'In this piece\'s tenth section, woodwinds repeat the pattern "quarter rest, four falling sixteenth notes, quarter rest," where the first sixteenth note is tenuto and the rest are staccato. As a joke, the viola melody in this piece\'s sixth section crosses directly from the fourth to the second string. Jagged, toccata-like chromatic runs in its second section depict an amateur pianist warming up. Most section titles of this piece are'
r1_q16_t2 = 'initials, like C. A. E., which represents its composer\'s wife Alice. Viola student Isabel Fitton and the stuttering Dorabella are two "friends pictured within" this piece. It may be based on "Auld Lang Syne" or "Rule Britannia." August Jaeger inspired its section "Nimrod."'
r1_q16_t3 = 'For 10 points, name this orchestral piece by Edward Elgar with an unknown theme.'
r1_q16_answer = 'Enigma Variations'
r1_q16 = get_or_create_question(Question(packet=round_1, text_part_1=r1_q16_t1,
                                         text_part_2=r1_q16_t2, text_part_3=r1_q16_t3, answer=r1_q16_answer, number=16))

r1_q17_t1 = 'The radar jamming system used by low-flying Vautour planes in Operation Focus during this war so spooked the otherwise uninvolved Soviets that Nikolai Yergorychev purged many Polish officers. In the build-up to this war, a strike killed 18 people at Al-Samu and UN Emergency Forces were ordered out of one country. One side lost 286 of its 420'
r1_q17_t2 = 'MiG fighters on the tarmac on a single day in this war. In the buildup to this conflict, the port of Eilat was cut off from supplies by the closure of the Gulf of Aqaba. The Sinai Peninsula, Golan Heights, and Gaza Strip were captured by the victors in this conflict, a defeat for Egypt\'s Gamal Abdel Nasser.'
r1_q17_t3 = 'For 10 points, name this 1967 conflict in which Israel defeated its enemies in less than a week.'
r1_q17_answer = 'Six-Day War'
r1_q17 = get_or_create_question(Question(packet=round_1, text_part_1=r1_q17_t1,
                                         text_part_2=r1_q17_t2, text_part_3=r1_q17_t3, answer=r1_q17_answer, number=17))

r1_q18_t1 = 'A defect in one enzyme in this pathway has a severe "Beppu" variant and causes echinocytes to appear on a peripheral smear. An enzyme that catalyzes the start of this pathway has three subtypes referred to as "low K-sub-m" isozymes for their increased affinity to their substrate, and also a fourth isozyme that is found only in the liver. Another enzyme in this pathway performs an aldol cleavage to form the intermediate DHAP. This pathway begins with'
r1_q18_t2 = 'substrate-level phosphorylation carried out by hexokinase and ends with two three-carbon molecules that are eventually converted into acetyl-CoA.'
r1_q18_t3 = 'For 10 points, name this first step of cellular respiration that cleaves glucose to create two pyruvate molecules.'
r1_q18_answer = 'glycolysis'
r1_q18 = get_or_create_question(Question(packet=round_1, text_part_1=r1_q18_t1,
                                         text_part_2=r1_q18_t2, text_part_3=r1_q18_t3, answer=r1_q18_answer, number=18))

r1_q19_t1 = 'In the first of these poems, the speaker asks that the addressee "like adamant draw mine iron heart." In a poem from this collection, the speaker claims to be made of "elements and an angelic sprite," which are "betray\'d to endless night," and calls himself "a little world made cunningly." Another of these poems declares that the speaker will never be "chaste, except you ravish me" and implores'
r1_q19_t2 = '"Break, blow, burn, and make me new." This collection includes a poem that calls the addressee "slave to fate, chance, kings, and desperate men," as well as a poem beginning "Batter my heart, three-person\'d God."'
r1_q19_t3 = 'For 10 points, name these nineteen religious poems, including "Death, Be Not Proud," written by John Donne.'
r1_q19_answer = 'Holy Sonnets'
r1_q19 = get_or_create_question(Question(packet=round_1, text_part_1=r1_q19_t1,
                                         text_part_2=r1_q19_t2, text_part_3=r1_q19_t3, answer=r1_q19_answer, number=19))

r1_q20_t1 = 'In advance of this event, a leader asked his cousin to cover himself in a green cloak and sleep in his bed. Historians identify the Axumite king Armah with a man involved in the so-called "first" version of this event, Ashama ibn Abjar, who sheltered several "sahaba". A place of worship at Quba was founded during this event, in which two men stopped and prayed on Friday in the first instance of'
r1_q20_t2 = '"jumu\'ah". The person who undertook this event ended up in Yathrib, which was renamed shortly afterward, and carried it out with Abu Bakr. This event, whose Julian date is April 19, 622 AD, marks the beginning of the Islamic calendar.'
r1_q20_t3 = 'For 10 points, name this flight of the prophet from one of Islam\'s holy cities to another.'
r1_q20_answer = 'Hijrah, Muhammad\'s flight from Mecca'
r1_q20 = get_or_create_question(Question(packet=round_1, text_part_1=r1_q20_t1,
                                         text_part_2=r1_q20_t2, text_part_3=r1_q20_t3, answer=r1_q20_answer, number=20))

r1_q21_t1 = 'The NINCDS-ADRDA criteria are used to diagnose this disease. The first person diagnosed with this disease was a woman named "Auguste D." Screens for this disease led to the discovery of presenilins, the catalytic subunits of gamma-secretase. The drug donepezil, sold under the brand name Aricept, is used to treat symptoms of this disease. Sufferers of this disease can exhibit neurofibrillary'
r1_q21_t2 = 'tangles due to hyper-phosphorylation of tau proteins. This disease can be caused by a mutation in the APP protein, which leads to the buildup of plaques of amyloid beta. This disease causes progressive cognitive impairment, shown by language and memory problems.'
r1_q21_t3 = 'For 10 points, name this neurodegenerative disease, the most common cause of dementia.'
r1_q21_answer = 'Alzheimer\'s'
r1_q21 = get_or_create_question(Question(packet=round_1, text_part_1=r1_q21_t1,
                                         text_part_2=r1_q21_t2, text_part_3=r1_q21_t3, answer=r1_q21_answer, number=21))


# 3. Packet for round two
round_2 = get_or_create_packet(Packet(tournament=tournament,
                                      name='Round 02', round_number=2, packet_type=PacketType.TOSSUP.name))

r2_q01_t1 = 'A 1958 book on the "method of theory" of the "American" form of this discipline stated the authors\' belief that this discipline is "anthropology or it is nothing." A 20th-century practitioner of this discipline adapted Robert Merton\'s idea of "middle range theories" to describe an approach to this discipline that involved ethnographic fieldwork among hunter-gatherer societies. Lewis Binford pioneered the "new," or'
r2_q01_t2 = '"processual," form of this discipline. The "Harris matrix" is a method of creating seriation diagrams in this discipline that rely on the laws of "original horizontality," "stratigraphic succession," and "superposition." Sites such as Göbekli Tepe and Cahokia are examined by practitioners of,'
r2_q01_t3 = 'for 10 points, what academic discipline concerning the excavation of human-built sites?'
r2_q01_answer = 'archaeology'
r2_q01 = get_or_create_question(Question(packet=round_2, text_part_1=r2_q01_t1,
                                         text_part_2=r2_q01_t2, text_part_3=r2_q01_t3, answer=r2_q01_answer, number=1))

r2_q02_t1 = 'Residents of a locale created by this author include Elias, who fails exams to be a doctor and a sanitary inspector before eventually becoming a cart driver, and a poet who fails to write anything past the first line of his magnum opus and is named B. Wordsworth. In another novel by this author, Father Huismans collects African masks, and a man who worships the cult of the Black Madonna takes over an unnamed town. The shopkeeper Salim lives in a country led by the'
r2_q02_t2 = 'Big Man in a novel by this man, who also wrote "Miguel Street" and a novel whose title character, an eleven-fingered sign-painter, marries into the overbearing Tulsi family.'
r2_q02_t3 = 'For 10 points, name this Indo-Trinidadian author of "A Bend in the River" and "A House for Mr. Biswas."'
r2_q02_answer = 'V. S. Naipaul'
r2_q02 = get_or_create_question(Question(packet=round_2, text_part_1=r2_q02_t1,
                                         text_part_2=r2_q02_t2, text_part_3=r2_q02_t3, answer=r2_q02_answer, number=2))

r2_q03_t1 = 'This man lends his name to a type of tree that legendarily won\'t bloom until kicked by a young woman. The "black" legends about this monarch hold that he killed 99 of his siblings. After his death, his throne was disputed by his sons Jaluka, Tivara, and Kunala. He may have abolished the death penalty and founded some 84,000 religious institutions. He convened a religious council at Pataliputra, and his son Mahendra brought a'
r2_q03_t2 = 'bodhi branch with him on a religious mission to Sri Lanka. Some monuments created by this man were inscribed in Brahmi, others were inscribed in Greek. His namesake Lion Capital now appears on a flag. This grandson of Chandragupta erected rock edicts following a conversion in Kalinga.'
r2_q03_t3 = 'For 10 points, name this Mauryan emperor who became a Buddhist.'
r2_q03_answer = 'Ashoka'
r2_q03 = get_or_create_question(Question(packet=round_2, text_part_1=r2_q03_t1,
                                         text_part_2=r2_q03_t2, text_part_3=r2_q03_t3, answer=r2_q03_answer, number=3))

r2_q04_t1 = 'Von Weizsäcker developed a functional to describe this quantity that is commonly used in Thomas–Fermi DFT. This quantity is transferred from large-scale to small-scale eddies in a Kolmogorov cascade. In time-of-flight mass spectrometry, all ions with the same charge will also have the same value of this quantity. By measuring this quantity for an emitted photoelectron, one can calculate the work function of a metal. This quantity equals "gamma minus one times'
r2_q04_t2 = 'm c-squared" in special relativity, and "p-squared divided by 2 m" in Newtonian mechanics. This quantity is conserved in elastic collisions but not inelastic collisions.'
r2_q04_t3 = 'For 10 points, name this quantity which equals one-half times mass times velocity squared and represents the energy of motion.'
r2_q04_answer = 'kinetic energy'
r2_q04 = get_or_create_question(Question(packet=round_2, text_part_1=r2_q04_t1,
                                         text_part_2=r2_q04_t2, text_part_3=r2_q04_t3, answer=r2_q04_answer, number=4))

r2_q05_t1 = 'This event begins in Cologne on the 11th hour of the 11th day of the 11th month, and in medieval times, it saw a ceremonial transfer of power to women. Popes Leo X and Clement VII both banned the practice of throwing rotten oranges at Jews who were forced to run naked through Rome during this event. Fastnachtsspiel plays were staged in Germany during this event. In France, this event typically began on Quinquagesima Sunday, while Bavarians start celebrating it after the'
r2_q05_t2 = 'Feast of the Epiphany. In many regions, this event is most commonly celebrated on Shrove Tuesday. The name of this festival may come from the Latin phrase "the pleasure of meat," as meat is forbidden in the season that follows it.'
r2_q05_t3 = 'For 10 points, name this merry Catholic festival that takes place prior to Lent.'
r2_q05_answer = 'carnival'
r2_q05 = get_or_create_question(Question(packet=round_2, text_part_1=r2_q05_t1,
                                         text_part_2=r2_q05_t2, text_part_3=r2_q05_t3, answer=r2_q05_answer, number=5))

r2_q06_t1 = 'This man developed a limp while participating in an invasion of Azamor in Morocco, and he defected from his country due to lack of royal compensation. Thirty members of this man’s crew were killed when they were ambushed at a banquet hosted by Humabon. The House of Trade sponsored a voyage by this man to find the Spice Islands that was chronicled by Antonio Pigafetta. This European\'s forces were defeated by chief Lapu-Lapu. 27 of his men died of'
r2_q06_t2 = 'scurvy before reaching the islands of Rota and Guam. This captain of the Trinidad died in the Philippines from a poisoned arrow to the leg. He led ships from the Atlantic to the Pacific Oceans through a body of water now named for him.'
r2_q06_t3 = 'For 10 points, name this man who died leading the first circumnavigation of the earth.'
r2_q06_answer = 'Ferdinand  Magellan'
r2_q06 = get_or_create_question(Question(packet=round_2, text_part_1=r2_q06_t1,
                                         text_part_2=r2_q06_t2, text_part_3=r2_q06_t3, answer=r2_q06_answer, number=6))

r2_q07_t1 = 'A play that won the Pulitzer Prize at the beginning of this decade depicts the reunion of the Magrath Sisters after Babe shot her husband; that play is Beth Henley\'s "Crimes of the Heart". A play set during this decade is the subject of Isaac Butler\'s and Dan Kois\'s "oral history" "The World Only Spins Forward". In that play set during this decade, characters named Oceania, Asiatica, Europa, and Antarctica meet in the Council Room of the Continental'
r2_q07_t2 = 'Principalities. That play set during this decade is divided into the two parts "Millennium Approaches" and "Perestroika," and opens with the revelation that Prior Walter has an incurable disease.'
r2_q07_t3 = 'For 10 points, name this decade that provides the setting for Tony Kushner\'s "Angels in America," which focuses on the AIDS epidemic.'
r2_q07_answer = '1980s'
r2_q07 = get_or_create_question(Question(packet=round_2, text_part_1=r2_q07_t1,
                                         text_part_2=r2_q07_t2, text_part_3=r2_q07_t3, answer=r2_q07_answer, number=7))

r2_q08_t1 = 'A piece in this genre slowly introduces the theme "E, E E E, F, E, C, E" for 4 bars before it is played in triads under long falling chromatic scales. It\'s not a lied, but a galloping horse reaches exhaustion in the slower "Animato" section of one of these pieces based on a Victor Hugo poem, which opens with a descent of broad, rolled diminished 7th chords before a cadenza. In one of these pieces, the right hand plays rapid triplets in G-flat major'
r2_q08_t2 = 'pentatonic. "La Campanella" is the third "Grand Paganini" piece in this genre by Franz Liszt , who composed "Mazeppa" in a set of "Transcendental" pieces in this genre. Frédéric Chopin performed ones nicknamed "Black Key" and "Revolutionary."'
r2_q08_t3 = 'For 10 points, name these pieces written to train musicians.'
r2_q08_answer = 'etudes'
r2_q08 = get_or_create_question(Question(packet=round_2, text_part_1=r2_q08_t1,
                                         text_part_2=r2_q08_t2, text_part_3=r2_q08_t3, answer=r2_q08_answer, number=8))

r2_q09_t1 = 'It\'s not electrophoresis, but running this technique, removing the solvent, rotating the system 90 degrees, and adding a new solvent is this technique\'s two-dimensional form. A polyhistidine tag and nickel, or GST and glutathione, are common methods of immobilizing biomolecules in the "affinity" version of this technique. Salt concentration is tightly controlled in the ion-exchange form of this technique, and broadening in it is described by the'
r2_q09_t2 = 'van Deemter equation. A column full of gel is used in this technique’s gel permeation type, while the HPLC type performs it at high pressure. Every technique of this kind has a stationary and a mobile phase.'
r2_q09_t3 = 'For 10 points, identify this technique that separates mixtures, such as ink on wet paper.'
r2_q09_answer = 'two dimensional chromatography'
r2_q09 = get_or_create_question(Question(packet=round_2, text_part_1=r2_q09_t1,
                                         text_part_2=r2_q09_t2, text_part_3=r2_q09_t3, answer=r2_q09_answer, number=9))

r2_q10_t1 = 'Kreiner showed the negative effects of this type of policy when Danish citizens turn 18. A 2016 law applies this type of policy only to Britons older than 25. Some 300,000 Albertans are slated to benefit from a change in this policy that mirrors one passed in 2014 by now-disgraced mayor Ed Murray. Researchers at Berkeley and the University of Washington put out rival studies in 2017 about whether this type of policy reduced available'
r2_q10_t2 = 'hours. SMIC, a French policy of this type, is adjusted each January based on factors such as the consumer price index. A "ten ten" policy of this type in the US would bring 900,000 people out of poverty, while one in Seattle may be negatively affecting restaurant jobs.'
r2_q10_t3 = 'For 10 points, name this policy that sets the lowest amount of money that a worker can legally be paid.'
r2_q10_answer = 'minimum wage'
r2_q10 = get_or_create_question(Question(packet=round_2, text_part_1=r2_q10_t1,
                                         text_part_2=r2_q10_t2, text_part_3=r2_q10_t3, answer=r2_q10_answer, number=10))

r2_q11_t1 = 'Description acceptable. A proposal that this process would occur on the "same terms" at the Constitutional Convention was defeated by Gouverneur Morris. John A. Burns, the architect of the most recent successful campaign for this result, was subsequently defeated by William F. Quinn in a 1959 gubernatorial race. Plural marriages were forbidden by a law that started this process, the Enabling Act of 1894. One unusual route to this process began with the 1861'
r2_q11_t2 = 'Wheeling Convention. This process is typically preceded by the writing and ratification of a constitution. It\'s not independence, but in 2012, 61 percent of voters supported starting this process in Puerto Rico.'
r2_q11_t3 = 'For 10 points, name this action which allowed the United States to expand beyond the original thirteen colonies.'
r2_q11_answer = 'admission of a new state to the Union'
r2_q11 = get_or_create_question(Question(packet=round_2, text_part_1=r2_q11_t1,
                                         text_part_2=r2_q11_t2, text_part_3=r2_q11_t3, answer=r2_q11_answer, number=11))

r2_q12_t1 = 'The so-called "Islamic Wing" of this institution was designed by Kevin Roche, the architect who has been responsible for all its expansions, and who created a new master plan for it in the 1970s. After Calvert Vaux\'s design for this building was criticized in 1871, a Beaux Arts-style grand stairway and facade designed by Richard Morris Hunt was installed near the end of the 19th century. A part of this institution in Fort Tryon Park devoted to subjects from the Middle Ages is called The'
r2_q12_t2 = 'Cloisters. This institution\'s main collection, which includes David\'s "The Death of Socrates" and Winslow Homer\'s "The Gulf Stream", is in a set of buildings on Fifth Avenue, between 81st and 84th streets.'
r2_q12_t3 = 'For 10 points, name this largest art museum in New York City.'
r2_q12_answer = 'Metropolitan Museum of Art'
r2_q12 = get_or_create_question(Question(packet=round_2, text_part_1=r2_q12_t1,
                                         text_part_2=r2_q12_t2, text_part_3=r2_q12_t3, answer=r2_q12_answer, number=12))

r2_q13_t1 = 'The amount of two isoforms of creatine kinase can be used to test for this condition in the CK-MB test. Sgarbossa\'s criteria can help to diagnose this condition, especially when it is complicated by the presence of a left bundle branch block. The levels of troponins T and I can indicate the presence of this condition. This condition can be classified into ST elevation and non-ST elevation types based on the result from an'
r2_q13_t2 = 'ECG. This condition can be caused by the buildup of cholesterol into plaques of coronary arteries, known as atherosclerosis. Common symptoms of this condition include shortness of breath and chest pain radiating up the left arm.'
r2_q13_t3 = 'For 10 points, name this condition in which blood flow stops to a part of the heart.'
r2_q13_answer = 'heart attack'
r2_q13 = get_or_create_question(Question(packet=round_2, text_part_1=r2_q13_t1,
                                         text_part_2=r2_q13_t2, text_part_3=r2_q13_t3, answer=r2_q13_answer, number=13))

r2_q14_t1 = 'In one novel by this author, the protagonist visits Brighton with the prostitute Milly and her daughter Winnie so that private detectives can give his wife evidence to divorce him. Another of this author\'s characters receives a turtle engraved with diamonds forming her initials from her husband Rex Mottram. In a novel by this author, the owner of Hetton Abbey is held captive in the Brazilian jungle by Mr. Todd, who forces him to'
r2_q14_t2 = 'read Dickens novels forever. In this author\'s most famous novel, Lord Marchmain\'s deathbed conversion inspires Julia to break with Charles Ryder, who is brought to the title estate by his friend Sebastian Flyte.'
r2_q14_t3 = 'For 10 points, name this satirical English novelist of "A Handful of Dust" and "Brideshead Revisited."'
r2_q14_answer = 'Evelyn Waugh'
r2_q14 = get_or_create_question(Question(packet=round_2, text_part_1=r2_q14_t1,
                                         text_part_2=r2_q14_t2, text_part_3=r2_q14_t3, answer=r2_q14_answer, number=14))

r2_q15_t1 = 'This philosopher recounted a parable by Zeno of Citium which compared the way the soul assents to a clear perception, or "katalepsis," to a fist. Macrobius wrote a Neoplatonic commentary on a passage by this philosopher in which Scipio is presented with visions of life after death and the nine celestial spheres. This philosopher discussed conflicts between honor and expediency in a Stoic-influenced essay for his son,'
r2_q15_t2 = '"De Officiis," and wrote a dialogue on Roman history and government called "De Re Publica." Petrarch\'s rediscovery of this man\'s letters in the 14th century reignited interest in classical culture.'
r2_q15_t3 = 'For 10 points, name this Roman statesman and orator whose denunciations of Marc Anthony in the "Philippics" led to his assassination.'
r2_q15_answer = 'Marcus Tullius Cicero'
r2_q15 = get_or_create_question(Question(packet=round_2, text_part_1=r2_q15_t1,
                                         text_part_2=r2_q15_t2, text_part_3=r2_q15_t3, answer=r2_q15_answer, number=15))

r2_q16_t1 = 'During a campaign to this modern-day country, Geoffroy Saint-Hilaire performed edifying shark dissections for crewmen. On the way to this non-island country, the namesake of the Dolomite Mountains secured the surrender of the Knights Hospitaller. 151 "savants" who joined a campaign here produced an encyclopedia called the "Description" of it. A general used the divisional square tactic and told troops that "40 centuries look down upon you" at a'
r2_q16_t2 = '1798 battle in this country. Horatio Nelson was non-fatally wounded in this country at the Battle of Aboukir Bay. During Napoleon\'s campaign in this country, a trilingual stele was found that helped decipher an ancient script.'
r2_q16_t3 = 'For 10 points, name this site of the Battle of the Pyramids.'
r2_q16_answer = 'Egypt'
r2_q16 = get_or_create_question(Question(packet=round_2, text_part_1=r2_q16_t1,
                                         text_part_2=r2_q16_t2, text_part_3=r2_q16_t3, answer=r2_q16_answer, number=16))

r2_q17_t1 = 'A man from Argos who has this occupation meets Telemachus in Sparta and hitches a ride to Ithaca with him. Another of these people takes a reviving herb from a snake after finding the body of the child Glaucus in a pot of honey. Theoclymenus and Polyidus did this job, as did a brother of Bias who pulled a knife out of a tree, then used it to heal the son of Anaxagoras. That man with this occupation heard two termites'
r2_q17_t2 = 'talking in his prison cell, warning him of its impending collapse. Melampus had this occupation, as did both Mopsus and his rival Calchas. Another of these characters spent seven years as a woman and served as an advisor in Thebes.'
r2_q17_t3 = 'For 10 points, identify the occupation of Tiresias and others who had visions of the future.'
r2_q17_answer = 'seers or prophets or augurs or soothsayers'
r2_q17 = get_or_create_question(Question(packet=round_2, text_part_1=r2_q17_t1,
                                         text_part_2=r2_q17_t2, text_part_3=r2_q17_t3, answer=r2_q17_answer, number=17))

r2_q18_t1 = 'A. J. R. Prentice theorized that this entity formed as a result of the shedding of systems of rings and tori of gas. This entity is treated as a dynamical system that evolves over time in the Nice model. Pierre-Simon Laplace proposed that this structure formed after a giant molecular cloud collapsed, creating a "disk" from which this structure\'s constituents formed. The'
r2_q18_t2 = 'Hill sphere is often used to define the boundaries of this structure, which extends beyond both TNOs and Kuiper belt objects. The farthest edge of the Oort Cloud and the heliopause have been proposed as alternate ways to define the boundaries of this set of objects.'
r2_q18_t3 = 'For 10 points, name this astronomical structure, which includes eight planets and the Sun.'
r2_q18_answer = 'the Solar System'
r2_q18 = get_or_create_question(Question(packet=round_2, text_part_1=r2_q18_t1,
                                         text_part_2=r2_q18_t2, text_part_3=r2_q18_t3, answer=r2_q18_answer, number=18))

r2_q19_t1 = 'This character gets a package on his birthday containing two books translated by Wetstein to replace his large, unwieldy Ernestine edition, as well as a pink ribbon. This character goes on to live a boring, everyday life after another character foils his plans with some pellets of chicken blood in a parody by Friedrich Nicolai. He resigns from a diplomatic job after an embarrassing incident in which he is snubbed by a group of aristocrats at a party held by'
r2_q19_t2 = 'Count C. After a scene in which he emotionally recites passages from Ossian, this character claims to be going on a "journey" into the mountains as a pretext to borrow a pair of pistols from Albert.'
r2_q19_t3 = 'For 10 points, name this character whose obsessive love for Lotte is the subject of a n early novel by Goethe.'
r2_q19_answer = 'Werther'
r2_q19 = get_or_create_question(Question(packet=round_2, text_part_1=r2_q19_t1,
                                         text_part_2=r2_q19_t2, text_part_3=r2_q19_t3, answer=r2_q19_answer, number=19))

r2_q20_t1 = 'A political cartoon from the Almanack of the Month depicted this man painting with a mop. He created several whale paintings for oil tycoon Elhanan Bicknell. Rachel Whiteread and Damien Hirst have both won a prize named for this artist awarded by the Tate. The National Gallery exhibits some of his paintings next to those of Claude Lorrain, an artist who inspired his seascape "Dido Building Carthage." In one of this artist\'s paintings, a'
r2_q20_t2 = 'rabbit rushes out of the way of a vehicle coming towards the viewer on the Maidenhead Railway Bridge. In another of his works, sharks pursue the chained bodies that have been thrown overboard by the captain of the title vessel.'
r2_q20_t3 = 'For 10 points, name this British landscape artist of "Rain, Steam and Speed" and "The Slave Ship."'
r2_q20_answer = 'J. M. W. Turner'
r2_q20 = get_or_create_question(Question(packet=round_2, text_part_1=r2_q20_t1,
                                         text_part_2=r2_q20_t2, text_part_3=r2_q20_t3, answer=r2_q20_answer, number=20))

r2_q21_t1 = 'In a story from the Jataka, lightning destroys a hunter\'s house as punishment for killing three of these beings, namely Nandiya, Jollikin, and their starving mother. A Japanese folktale depicts one of them being revenge-killed by the children of a crab. One of these beings marries the widowed Tara after defeating his own brother to become the king of Kishkindha. A deity who resembled this animal was conceived when his mother ate divine cake sent by the wind god Vayu; that deity once once'
r2_q21_t2 = 'lifted an entire mountain while searching for an herb. Sugriva and other vanaras are generally depicted in the form of this animal, as was a deity who destroyed Lankapuri after Ravana\'s guards set his tail on fire.'
r2_q21_t3 = 'For 10 points, name this type of animal, whose form is taken by Hanuman.'
r2_q21_answer = 'monkeys'
r2_q21 = get_or_create_question(Question(packet=round_2, text_part_1=r2_q21_t1,
                                         text_part_2=r2_q21_t2, text_part_3=r2_q21_t3, answer=r2_q21_answer, number=21))

# 4. Packet for round three
round_3 = get_or_create_packet(Packet(tournament=tournament,
                                      name='Round 03', round_number=3, packet_type=PacketType.TOSSUP.name))

r3_q01_t1 = 'A character in this play accuses another man of just hitting "younger men... and children... women... birds." Another character in this play tells the story of a fifteen-year old boy who accidentally killed his mother with a shotgun, and who caused much laughter by ordering "bergin and water." In another story about that boy in this play, he was taken to the hospital after he crashed his car while'
r3_q01_t2 = 'swerving to avoid a porcupine in the road. In this play, a "hysterical pregnancy" supposedly caused Nick to marry his wife. During the "Walpurgisnacht" act of this play, George suggests that a game of "Get the Guests" be played to humiliate Martha and Honey.'
r3_q01_t3 = 'For 10 points, name this domestic drama by Edward Albee.'
r3_q01_answer = 'Who\'s Afraid of Virginia Woolf?'
r3_q01 = get_or_create_question(Question(packet=round_3, text_part_1=r3_q01_t1, text_part_2=r3_q01_t2, text_part_3=r3_q01_t3, answer=r3_q01_answer, number=1))

r3_q02_t1 = 'Calcium copper titanate is a particularly strong one of these materials due to a grain boundary. Energy dissipation in these materials is quantified by the loss tangent. Implicit models of solvation treat the solvent as one of these materials, which name a quantity used to measure solvent polarity. The namesake "strength" of these materials is measured in volts per meter and gives the applied field needed to make them conduct above the'
r3_q02_t2 = 'breakdown voltage. A quantity named for these materials is also called "relative permittivity" and is multiplied by epsilon-naught times area over distance in the parallel-plate model.'
r3_q02_t3 = 'For 10 points, what insulating materials are placed between the plates of a capacitor to increase capacitance?'
r3_q02_answer = 'dielectrics'
r3_q02 = get_or_create_question(Question(packet=round_3, text_part_1=r3_q02_t1, text_part_2=r3_q02_t2, text_part_3=r3_q02_t3, answer=r3_q02_answer, number=2))

r3_q03_t1 = 'One of the first stars in this profession collaborated on some projects with Reform Club member and architect Charles Barry and was named Alexis Soyer. Massimo Bottura wrote a 2011 book titled for people in this profession, some of whom run businesses called "trattoria." These people often wear a starched hat called a "toque blanche." In the US, the'
r3_q03_t2 = 'James Beard foundation gives out awards to people in this profession. In 2012, one of these people named Bernard Loiseau killed himself amidst rumors that he would be downgraded from three to two Michelin stars. Auguste Escoffier\'s hierarchy of this profession puts their "sous" variety second in command.'
r3_q03_t3 = 'For 10 points, an apron is usually worn by members of what food preparation profession?'
r3_q03_answer = 'chef or cook'
r3_q03 = get_or_create_question(Question(packet=round_3, text_part_1=r3_q03_t1, text_part_2=r3_q03_t2, text_part_3=r3_q03_t3, answer=r3_q03_answer, number=3))

r3_q04_t1 = 'This organization was likened to a cult in the title of a 1974 book by Victor Marchetti. It\'s not the NSC, but in 1946 Harry Truman appointed Sidney Souers to be this organization\'s first leader. Its one-time leader William Colby devised many of the "stay-behinds" for Operation Gladio. Its "Family Jewels" documents were released to the public during the'
r3_q04_t2 = 'Church Committee hearings, in which Mary Embree claimed that this organization developed a "heart attack gun." Gerald Ford appointed George H. W. Bush to serve as its director in the 1970s. This organization succeeded the Office of Strategic Services and generally lacks a domestic charter.'
r3_q04_t3 = 'For 10 points, name this US government agency that gathers information about foreign espionage.'
r3_q04_answer = 'CIA or the Central Intelligence Agency'
r3_q04 = get_or_create_question(Question(packet=round_3, text_part_1=r3_q04_t1, text_part_2=r3_q04_t2, text_part_3=r3_q04_t3, answer=r3_q04_answer, number=4))

r3_q05_t1 = 'A character in this play is asked about the views of Pythagoras on birds and believes himself to be the addressee of a letter written to "M, O, A, I." That character in this play is asked if he thinks, because he is virtuous, "there shall be no more cakes and ale?" After being locked in a room, that character in this play is visited by a man disguised as the priest Sir Topas, who insists that character has gone'
r3_q05_t2 = 'mad. The primary subplot in this play revolves around a forged love letter from Olivia that tricks the prudish servant Malvolio.'
r3_q05_t3 = 'For 10 points, name this play about the shipwrecked Viola and Sebastian, a Shakespearean comedy named for the fact that it was originally performed at the end of Christmas festivities.'
r3_q05_answer = 'Twelfth Night'
r3_q05 = get_or_create_question(Question(packet=round_3, text_part_1=r3_q05_t1, text_part_2=r3_q05_t2, text_part_3=r3_q05_t3, answer=r3_q05_answer, number=5))

r3_q06_t1 = 'Angelo Tani commissioned a painting of this scene that ended up in Poland after Paul Benecke captured the ship transporting it. St. Peter shakes hands with one of the naked men in a procession in the left-hand side of an altarpiece of this scene by Hans Memling. One version of this scene was altered by "Il Braghettone," Daniele da Volterra. The artist of one version of this scene depicted himself as the man holding his'
r3_q06_t2 = 'own flayed skin, St. Bartholomew. Memling\'s version of this scene depicts an armor-clad Michael in the foreground. This scene decorates the altar wall of a building that Michelangelo had earlier painted the ceiling for.'
r3_q06_t3 = 'For 10 points, name this Biblical scene of Christ sending souls to Heaven and Hell.'
r3_q06_answer = 'The Last Judgment'
r3_q06 = get_or_create_question(Question(packet=round_3, text_part_1=r3_q06_t1, text_part_2=r3_q06_t2, text_part_3=r3_q06_t3, answer=r3_q06_answer, number=6))

r3_q07_t1 = 'Removing three holes from one of these objects creates a topological surface called the "pair of pants." A Morin surface is formed by manipulating one of these objects, and David Hilbert illustrated that all geodesics on this structure are closed curves. The number of these objects that can touch another one of these objects is known as the'
r3_q07_t2 = 'kissing number. Johannes Kepler proposed a famous conjecture about the optimal packings for this structure in three-dimensional space. A coordinate system named after this object represents points as a distance, a polar angle, and an azimuthal angle.'
r3_q07_t3 = 'For 10 points, name this object that consists of all points in three-dimensional space that are equidistant to a given point.'
r3_q07_answer = 'sphere'
r3_q07 = get_or_create_question(Question(packet=round_3, text_part_1=r3_q07_t1, text_part_2=r3_q07_t2, text_part_3=r3_q07_t3, answer=r3_q07_answer, number=7))

r3_q08_t1 = 'A Homeric hymn to this deity ends with him being advised to visit a trio of honeycomb-eating nymphs at Parnassus called the Thriae; that poem also describes him encountering an old man on the plain of Onchestus after weaving some sandals. Aeneas\'s ally Evander was a son of this god. The nymph Salmacis fell in love with, and then merged with, a son of this god. An esoteric religious tradition based on texts attributed to this god dubbed him'
r3_q08_t2 = '"thrice-great." This father of the thief Autolycus used a strategy involving reversing footprints to successfully steal cattle belonging to another god, to whom this god gave the lyre as compensation. A snake-wrapped staff called the "caduceus" was carried by,'
r3_q08_t3 = 'for 10 points, what winged-sandal-wearing Greek messenger god?'
r3_q08_answer = 'Hermes'
r3_q08 = get_or_create_question(Question(packet=round_3, text_part_1=r3_q08_t1, text_part_2=r3_q08_t2, text_part_3=r3_q08_t3, answer=r3_q08_answer, number=8))

r3_q09_t1 = 'In the early 2000s, environmentalists successfully diverted a Transneft oil pipeline from passing within 3,000 feet of this body of water. A polluting pulp and paper mill on its banks was closed in 2013. A first millennium BC stele near this lake shows a giant lizard-like monster similar to the cryptid Lusud-Khan said to live here. The Buryat people who live around this lake refer to it as the "blue eye." This lake is threatened by a plan to open a uranium plant in'
r3_q09_t2 = 'Angarsk. The Selenga river flows into this lake, which is home to nerpa seals. The 45-mile-long island of Olkhon is located in this lake. It is both the oldest freshwater lake on Earth and, at 1,620 meters, the deepest.'
r3_q09_t3 = 'For 10 points, name this Siberian lake.'
r3_q09_answer = 'Lake Baikal'
r3_q09 = get_or_create_question(Question(packet=round_3, text_part_1=r3_q09_t1, text_part_2=r3_q09_t2, text_part_3=r3_q09_t3, answer=r3_q09_answer, number=9))

r3_q10_t1 = 'The victorious forces at this battle had to wait a month at the mouth of the Dives River for favorable weather. At a ceremony conducted on the Christmas Day following this battle, its victor\'s troops set fire to nearby buildings after mistaking cries of acclamation for insurrection. The Battle Abbey was built to commemorate this battle, which was the culmination of a campaign begun at Pevensey. Two years after this battle, the victor wrought destruction on territories beyond the'
r3_q10_t2 = 'River Humber in the Harrying of the North.The losing side in this battle had just fought the Battle of Stamford Bridge. The loser of this battle is depicted taking an arrow to the eye in the Bayeux Tapestry.'
r3_q10_t3 = 'For 10 points, name this 1066 victory for William the Conqueror.'
r3_q10_answer = 'Battle of Hastings'
r3_q10 = get_or_create_question(Question(packet=round_3, text_part_1=r3_q10_t1, text_part_2=r3_q10_t2, text_part_3=r3_q10_t3, answer=r3_q10_answer, number=10))

r3_q11_t1 = 'A protein in the HSP70 family that is localized to the ER is named for "binding" to these molecules. The kinetoplast of "Crithidia luciliae" is used to detect examples of these entities that bind to dsDNA. The binding of these proteins to their substrates can produce C3 convertase and trigger the classical complement pathway. These proteins are used to visualize indirect fluorescence, in which'
r3_q11_t2 = 'secondary types of these proteins bind primary ones in a technique commonly used with Western blots. One of these proteins, rheumatoid factor, binds to the Fc region of another of these proteins. These proteins, made of two heavy chains and two light chains, are secreted by B cells.'
r3_q11_t3 = 'For 10 points, name these Y-shaped proteins which bind to antigens.'
r3_q11_answer = 'antibodies'
r3_q11 = get_or_create_question(Question(packet=round_3, text_part_1=r3_q11_t1, text_part_2=r3_q11_t2, text_part_3=r3_q11_t3, answer=r3_q11_answer, number=11))

r3_q12_t1 = 'Scholars dispute whether Marie-Anne Collot sculpted the face of a statue of this man. A mechanism for transporting part of a statue of this person was figured out by a Greek fugitive named Marinos Carburis. This ruler hired architect Domenico Trezzini to create buildings such as the Twelve Colleges. A monument to this man was the first since Pietro Tacca\'s statue of Philip IV to depict a freestanding'
r3_q12_t2 = 'bronze man on a rearing horse; that statue stands on a 1,250-tonne pedestal known as the Thunder Stone. This ruler is depicted in Étienne Maurice Falconet\'s "The Bronze Horseman," a statue in Senate Square in the city he founded, which is also home to the Hermitage Museum.'
r3_q12_t3 = 'For 10 points, name this Russian Emperor, the namesake of a major city on the Baltic Sea.'
r3_q12_answer = 'Peter the Great'
r3_q12 = get_or_create_question(Question(packet=round_3, text_part_1=r3_q12_t1, text_part_2=r3_q12_t2, text_part_3=r3_q12_t3, answer=r3_q12_answer, number=12))

r3_q13_t1 = 'In a letter opposing a lowered interest ceiling, this philosopher outlined an early quantity theory of money. This thinker argued that spoilage prevented accumulation until the invention of money in a work where he wrote that "In the beginning all the world was America." He stated that people gain a right to land by improving it as long as it is abundant, which Robert Nozick described as this man\'s "proviso." One work by this man argues that men cannot enter into'
r3_q13_t2 = 'slavery because they do not have absolute power over themselves, and is paired with a work that legitimizes revolutions against governments that lack the consent of the people.'
r3_q13_t3 = 'For 10 points, name this philosopher who defended the right to "life, liberty, and estate" in his "Two Treatises of Government."'
r3_q13_answer = 'John Locke'
r3_q13 = get_or_create_question(Question(packet=round_3, text_part_1=r3_q13_t1, text_part_2=r3_q13_t2, text_part_3=r3_q13_t3, answer=r3_q13_answer, number=13))

r3_q14_t1 = 'The historian Richard W. Bulliet examined the military advantage offered by these animals in a book that paired them with the wheel. A corps named for these animals established by Henry C. Wayne was used for carrying mail at Fort Mohave but was shuttered due to associations with Jefferson Davis. In a battle named for these animals, Talha and Zubair were killed leading a rebel army. In that 656 CE battle named for these animals,'
r3_q14_t2 = 'Aisha was captured by the caliph Ali. The salty milk from these animals is drunk by Bedouins. One of these animals was accidentally shot in the head at the Battle of Aqaba by its rider, T. E. Lawrence.'
r3_q14_t3 = 'For 10 points, name these animals, the dromedary variety of which are often used for desert travel.'
r3_q14_answer = 'camels'
r3_q14 = get_or_create_question(Question(packet=round_3, text_part_1=r3_q14_t1, text_part_2=r3_q14_t2, text_part_3=r3_q14_t3, answer=r3_q14_answer, number=14))

r3_q15_t1 = 'A soldier born in this country wrote an epic poem translated into English as "The Araucaniad." An ornate style of poetry from this country that took its name from a combination of the words for "cultured" and "Lutheran" was propounded most notably by the author of the unfinished poem "Solitudes." That poet engaged in a long-running feud with this country\'s leading proponent of "conceptism." The 300th anniversary of the death of a poet from this country inspired the founding of its'
r3_q15_t2 = 'Generation of \'27. A literary era in this country is often said to have ended with the death of the author of the plays "Life is a Dream" and "The Mayor of Zalamea."'
r3_q15_t3 = 'For 10 points, name this country whose Baroque "Golden Age" featured the authors Luis de Góngora and Pedro Calderón de la Barca.'
r3_q15_answer = 'Spain'
r3_q15 = get_or_create_question(Question(packet=round_3, text_part_1=r3_q15_t1, text_part_2=r3_q15_t2, text_part_3=r3_q15_t3, answer=r3_q15_answer, number=15))

r3_q16_t1 = 'Scattering experiments performed on these molecules are interpreted in Kratky or Guinier plots. The synthesis of these molecules by the ROMP reaction involves the relief of ring strain. Molecules can be "masked" from the immune system by attaching one of these molecules in the process of PEGylation. The telechelic versions of these molecules contain reactive'
r3_q16_t2 = 'end groups. These molecules can form through "living" reaction mechanisms that propagate through anionic, cationic, or radical intermediates. The polydispersity index characterizes their mass distribution, and DuPont created one of them from chloroprene.'
r3_q16_t3 = 'For 10 points, name these molecules which can be formed by step-growth or chain-growth mechanisms, which include neoprene and nylon.'
r3_q16_answer = 'polymers'
r3_q16 = get_or_create_question(Question(packet=round_3, text_part_1=r3_q16_t1, text_part_2=r3_q16_t2, text_part_3=r3_q16_t3, answer=r3_q16_answer, number=16))

r3_q17_t1 = 'A set of three sacred examples of these features is found at Dewa and is venerated by a sect founded by En no Gyoja. Worship of these features was incorporated into Shugendo, some practitioners of which are named for prostrating themselves at these features. Yamabushi are considered mystics of these features. One of them named Hiei was the site of the Enryaku-ji monastery, which was razed by Oda Nobunaga. An hourglass-shaped one of these features, which'
r3_q17_t2 = 'measures 80,000 yojanas in height and is named Sumeru is the axis-mundi in Buddhism. Along with flowers, one of these features was represented by Sakuya-hime; that example of these features contains a crater with "eight sacred peaks."'
r3_q17_t3 = 'For 10 points, Fuji is an example of what kind of landform?'
r3_q17_answer = 'mountains or volcanoes'
r3_q17 = get_or_create_question(Question(packet=round_3, text_part_1=r3_q17_t1, text_part_2=r3_q17_t2, text_part_3=r3_q17_t3, answer=r3_q17_answer, number=17))

r3_q18_t1 = 'An 1890 concession gave Gerald Talbot a monopoly over this crop in Iran, sparking an riot in Tehran. A boycott of the Austrian government\'s monopoly over this product sparked the Five Days of Milan in 1848. The leading merchants of 18th-century Glasgow were known as the "lords" of this crop. The use of this crop was dubbed "loathsome to the eye" and "harmful to the brain" in a treatise titled for a'
r3_q18_t2 = '"Counterblaste" to it by James I of England. Along with sugar and cotton, this crop was the chief export to England via the triangular trade; in England, it was popularized by Walter Raleigh after John Rolfe made it a cash crop in Virginia.'
r3_q18_t3 = 'For 10 points, name this plant, a chief ingredient in cigarettes.'
r3_q18_answer = 'tobacco'
r3_q18 = get_or_create_question(Question(packet=round_3, text_part_1=r3_q18_t1, text_part_2=r3_q18_t2, text_part_3=r3_q18_t3, answer=r3_q18_answer, number=18))

r3_q19_t1 = 'A string quartet inspired by this event begins and ends with the violins imitating the beeping sound made by a phone left off the hook. A piece inspired by this event quotes the trumpet solo from "The Unanswered Question" above a chorus singing the line "we all love you." In that piece, a boy repeats the word "missing" while pre-recorded voices repeat the names of this event\'s victims. The album cover of a Steve Reich string quartet named for this event controversially used a'
r3_q19_t2 = 'photo of it. The 2003 Pulitzer Prize for Music was awarded to a piece commemorating this event, "On the Transmigration of Souls." In the days after this event, popular musicians organized "The Concert for New York City."'
r3_q19_t3 = 'For 10 points, name this terrorist attack in 2001.'
r3_q19_answer = '9/11 or September 11, 2001'
r3_q19 = get_or_create_question(Question(packet=round_3, text_part_1=r3_q19_t1, text_part_2=r3_q19_t2, text_part_3=r3_q19_t3, answer=r3_q19_answer, number=19))

r3_q20_t1 = 'This novel\'s protagonist uses scrap from a man\'s old "yellow dress" to make the "Sister\'s Choice" pattern for her quilt. Another character in this novel moves to Tucson, Arizona after falling in love with the flute player Germaine. A character in this novel demands to be called Mary Agnes and not Squeak after she is raped by a prison warden. This novel ends during a family reunion on July 4th after the protagonist\'s sister returns from'
r3_q20_t2 = 'Africa, where she lived with the missionaries Samuel and Corinne. In this novel, "Mister" hides letters that are written by Nettie and addressed to her sister.'
r3_q20_t3 = 'For 10 points, name this novel in which Celie addresses many of her letters about life in southern Georgia to God, a novel by Alice Walker.'
r3_q20_answer = 'The  Color Purple'
r3_q20 = get_or_create_question(Question(packet=round_3, text_part_1=r3_q20_t1, text_part_2=r3_q20_t2, text_part_3=r3_q20_t3, answer=r3_q20_answer, number=20))

r3_q21_t1 = 'Eugène Delacroix may be the artist standing next to the bishop in this artist\'s enigmatic "The Eternal Feminine." A group of artists admire one of this artist\'s paintings in an "Homage" to him painted by Maurice Denis. His break from traditional forms of representation is examined in an essay on his "Doubt" by Maurice Merleau-Ponty. This artist often depicted one of his frequent subjects above an Aix-Marseille railway bridge. A leering man watches a black woman revealing the title'
r3_q21_t2 = 'woman in this artist\'s "A Modern Olympia." Pablo Picasso called this artist "the father of us all" and drew inspiration from this artist\'s many "Bathers" to develop Cubism.'
r3_q21_t3 = 'For 10 points, name this Post-Impressionist French artist who frequently painted still lifes of apples and views of Mont Sainte-Victoire.'
r3_q21_answer = 'Paul Cézanne'
r3_q21 = get_or_create_question(Question(packet=round_3, text_part_1=r3_q21_t1, text_part_2=r3_q21_t2, text_part_3=r3_q21_t3, answer=r3_q21_answer, number=21))

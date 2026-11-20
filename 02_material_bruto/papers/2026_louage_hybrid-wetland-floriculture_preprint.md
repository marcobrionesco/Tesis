# Texto extraído — 2026_louage_hybrid-wetland-floriculture_preprint

```text

=== PÁG 1 ===
 
1 
 
Performance evaluation and process 
1 
optimization of a hybrid treatment wetland 
2 
for nutrient rich floriculture drainage water 
3 
Flor Louage1*, Perry Hoendervangers1,2,3, Dion van Oirschot4, Dores G. Cirne2, Pieter Spanoghe3, Stijn 
4 
W.H. Van Hulle1, Diederik P.L. Rousseau1 
5 
1 Laboratory for Industrial Water and Eco Technology, Department of Green Chemistry and 
6 
Technology, Ghent University, Graaf Karel de Goedelaan 46, 8500 Kortrijk, Belgium 
7 
2 Vlaamse Instelling voor Technologisch Onderzoek, Boeretang 200, 2400 Mol, Belgium 
8 
3 Laboratory of Crop Protection Chemistry, Department of Plants and Crops, Ghent University, Coupure 
9 
Links 653, 9000 Ghent, Belgium 
10 
4 Rietland B.V., Van Aertselaerstraat 70, 2322 Minderhout, Belgium 
11 
*corresponding author: Flor.Louage@ugent.be 
12 
Abstract 
13 
This case study describes over three years of operation, monitoring and process control of a novel 
14 
hybrid treatment wetland (TW) treating nutrient-rich wastewater from a closed-loop hydroculture 
15 
system. The influent contained high nutrient concentrations i.e. TN 115.6 ± 34.7 mg L-1 and TP 18.5 ± 
16 
5.3 mg L-1 and a low carbon availability 22 ± 17 mg L-1 BOD. Discharge standards were imposed at 15 
17 
mg TN L-1 and 2 mg TP L-1. The hybrid TW consisted of an aerated TW (ATW) for nitrification followed 
18 
by three surface flow (SF) TWs designed to support denitrification via carbon inputs from plant 
19 
detritus. Detritus-driven denitrification in the SF TWs was sufficient only summer and early autumn. 
20 
During other periods, plant-based carbon input was inadequate and supplemental dosing of a liquid 
21 

=== PÁG 2 ===
 
2 
 
carbon source (LCS) was required to achieve TN standards. LCS addition was controlled using an online 
22 
water temperature sensor.  
23 
Phosphate was removed in a unit filled with crushed autoclaved aerated concrete (CAAC). After 770 
24 
days of operation, the TP discharge standard was reached, corresponding to an orthophosphate 
25 
adsorption capacity of 17.6 ± 6.7 g P kg-1. 
26 
Pesticide removal was also evaluated. Azoxystrobin, boscalid, and difenoconazole exceeded 0.1 µg L-1 
27 
in the influent. Azoxystrobin was mainly removed in the ATWs, boscalid in the SF units and ATW2, 
28 
while difenoconazole declined progressively across all treatment units except LCS-dosing and CAAC 
29 
units. 
30 
Overall, the hybrid TW effectively treated nutrient-rich industrial wastewater while providing 
31 
substantial pesticide removal, demonstrating its suitability for treatment in the floriculture sector. 
32 
 
33 
Keywords: Hybrid treatment wetlands; aeration; denitrification; carbon dosing; phosphorus 
34 
adsorption; pesticide removal 
35 
 
 
36 

=== PÁG 3 ===
 
3 
 
1 Introduction 
37 
The flower and ornamental horticulture industry (i.e. floriculture) in Flanders (northern region of 
38 
Belgium) had a production value of 208 million EUR in 2022, representing 3.3% of the total Flemish 
39 
agricultural production value in that year [1]. Greenhouses accounted for 45% of the sector surface 
40 
area [2] and rely on hydroculture for fertigation [3]. A closed-loop hydroculture system, where process 
41 
water is partly reused, saves up to 90 % water [4,5] and utilizes up to 85% less nutrients [5,6] compared 
42 
to open hydroculture. However, process must eventually be discharged due to salt accumulation [3,7]. 
43 
Floriculture wastewater typically contains high concentrations of nutrients, e.g. nitrogen (100 – 300 
44 
mg NO3--N L-1 ) and phosphorus (15 – 100 mg PO43--P L-1 ), and may also contain several pesticides 
45 
[3,8,9]. Untreated discharge of this wastewater causes negative impacts to the environment, such as 
46 
eutrophication and toxicity [10,11].  
47 
Specifically, Flanders is subjected to the EU water framework directive (WFD, 2000/60/EC), which 
48 
requires surface water bodies to reach good quality by 2027. To meet this objective, Flanders ratified 
49 
environmental quality standards [12]. Consequently, industrial wastewater discharge to surface water 
50 
bodies is only allowed with an environmental permit specifying flow limits and water quality 
51 
parameters. As of 2024, only one out of 196 surface water bodies in Flanders reached the good quality 
52 
according to the WFD [13]. As a response, more stringent discharge standards are stipulated in new or 
53 
renewed environmental permits. This study examines the case of a floriculture enterprise in Flanders, 
54 
following permit renewal, was required to comply with stringent effluent water quality discharge 
55 
standards. Specifically the nutrients total nitrogen (TN) (15 mg L-1) and total phosphorus (TP) (2 mg L-
56 
1). The wastewater originated from periodic discharges of closed-loop hydroponic cultivation (i.e. 
57 
fertigation) and occasional cleaning events. Household wastewater (i.e. from offices and the canteen) 
58 
is collected and treated separately and not further considered in this study. In view of its activities and 
59 
a broader commitment to sustainability, the company chose to implement a nature-based wastewater 
60 
treatment solution, namely a treatment wetland (TW).  
61 

=== PÁG 4 ===
 
4 
 
Indeed, TWs are a proven technology for full-scale treatment of various types of wastewaters [14], 
62 
including agriculture [15,16] and industrial wastewaters [17,18]. However, a large footprint is required 
63 
compared to more intensive wastewater technologies [19], which is an important constraint in 
64 
Flanders as it is a densely populated region with limited land availability. In addition, few to no full-
65 
scale TWs have been reported to reach 15 mg TN L-1  and 2 mg TP L-1 discharge standards from industrial 
66 
high nutrient concentrations without additional unit processes or intensification [3,18,20,21]. 
67 
Intensification of TWs can be achieved by incorporating performance-enhancing components, such as 
68 
mechanical aeration or targeted substance addition within the system [22,23]. This study incorporates 
69 
a more than 3 years monitoring and optimization of a novel full-scale hybrid TW. 
70 
Nitrogen in fertilizer-rich horticulture wastewater is present in different forms: organically bound (e.g. 
71 
urea); ammonium (NH4+), nitrite (NO2-) and nitrate (NO3-). Therefore, combining an aerobic step 
72 
followed by an anoxic step creates optimal conditions for biological nitrogen removal through 
73 
nitrification-denitrification [24,25]. Nitrification can be space-efficiently achieved by using an aerated 
74 
TW (ATW), which provide enhanced oxygen transfer [26,27]. The aerobic conditions also promote 
75 
heterotrophic carbon removal [25], which is unwanted as the COD/N ratio in floriculture wastewater 
76 
is already unfavorable for denitrification [8,9,28]. Additional carbon is therefore required to support 
77 
denitrification. In the case of TWs, carbon can be supplied through plant decay (i.e. detritus) [29]. 
78 
Surface flow (SF) TWs are preferred over subsurface TWs for carbon release from detritus, because the 
79 
decomposition occurs in the water column rather than on the TW surface [30]. Carbon input from 
80 
detritus varies over time due to factors such as season or growth phase [28], age of a TW [28], planting 
81 
density at start-up [31] and the selected plant species [32,33]. Carbon availability may therefore be 
82 
insufficient denitrification unless a very large TW areas are used, which conflicts existing space 
83 
constraints.  
84 
An alternative could be dissolved liquid carbon dosing [34], especially to bridge the colder winter 
85 
period when carbon input from detritus is lower [27]. Several studies have shown that carbon dosing 
86 

=== PÁG 5 ===
 
5 
 
can substantially enhance denitrification at low temperatures. Woodchip bioreactors have been 
87 
successfully operated as low as 5.5 °C [35] and acetate dosing has achieved up to fivefold higher nitrate 
88 
removal rates below 12 °C compared to systems without carbon addition [32]. However, carbon dosing 
89 
can lead to carbon leaching from the reactor [32]. In an ATW, optimal denitrification was reported at 
90 
a COD/NO3--ratio of 4 at 14 °C, whereas lower temperatures (10 - 12 °C) at a reduced COD/NO3--ratio 
91 
of 2, showed no significant effect of carbon dosing [27]. 
92 
Phosphorus removal in TWs can occur via plant uptake and plant biomass harvesting but is typically 
93 
rather limited unless large TW are used [24,36]. Microbial uptake and soil sorption immobilize 
94 
phosphorus rather than removing it from the system [36]. Reactive media can enhance phosphorus 
95 
removal but have a limited sorption capacity and require periodic replacement, which can be 
96 
facilitated by modular filter designs [36,37]. Reported adsorbent materials include crushed autoclaved 
97 
aerated concrete (CAAC) [38], iron oxide coated sand [37] and apatite [39], but more are described in 
98 
literature.  
99 
In addition to nutrients, floriculture wastewater may contain various pesticide residues which are used 
100 
to limit or prevent production losses from insects and fungi [40]. The discharge of pesticide-containing 
101 
wastewater poses risks to aquatic ecosystems due to toxicity at low concentrations, broad-spectrum 
102 
toxicity and persistence [41,42]. Pesticides can be removed from wastewater with TWs through 
103 
multiple mechanisms, primarily adsorption to substrate [43] and biodegradation [43], as well as other 
104 
mechanisms such as plant uptake [44], photodegradation [43], hydrolysis [45], volatilization [43]. 
105 
Though pesticide removal by full-scale TWs has been documented for a wide range of water types, e.g. 
106 
agricultural tailwater [46], studies concerning floriculture wastewater remain scarce.  
107 
To address the need for sustainability, land-use efficiency, and stringent nutrient discharge 
108 
requirements, a full-scale hybrid TW was developed for a floriculture company. The design integrated 
109 
ATWs for nitrification, SFs for carbon input through plant detritus, additional liquid carbon dosing to 
110 
promote denitrification, and reactive media for phosphorus removal. This study aimed to monitor and 
111 

=== PÁG 6 ===
 
6 
 
optimize the hybrid TW to consistently meet discharge standards (Table 2). The objectives of this study 
112 
were therefore: (1) to investigate whether the treatment system was capable of treating the fertilizer-
113 
rich horticulture wastewater and meeting discharge standards (in particular for nitrogen and 
114 
phosphorus); (2) to investigate whether optimization of the treatment train is possible and (3) to 
115 
monitor pesticides throughout the treatment system, allowing for elucidation of the pesticide removal 
116 
performance of each individual treatment unit.  
117 
 
 
118 

=== PÁG 7 ===
 
7 
 
2 Materials and methods 
119 
2.1 Site description 
120 
A floriculture company located in Flanders, Belgium was granted an environmental permit that allowed 
121 
the discharge of maximum 15 m3 d-1 of treated wastewater into a local stream, provided that stringent 
122 
nutrient standards were met (Table 2). To comply with these standards, a hybrid and intensified TW 
123 
consisting of multiple different treatment units was implemented (Figure S 1). System operation was 
124 
automated by coupling sensors and actuators to a programmable logic controller (PLC) (LOGO!, 
125 
Siemens, Germany). The system was put into operation in September 2021. 
126 
Wastewater from the hydroculture cultivation in the greenhouses and cleaning activities was collected 
127 
in a 223 m³ buffer tank (Table 1). From this tank, maximally 15 m³ d-1 of wastewater was intermittently 
128 
pumped onto the first aerated TW (ATW1), a Forced Bed Aeration® unit [47]. In this ATW1, perforated 
129 
pipes were installed along the bottom of the bed, through which air was diffused by a blower (JDK- S 
130 
150, Secoh, China).The wastewater was distributed on top of the full surface of ATW1 (Length (L) 4 m 
131 
x Width (W) 5 m x Depth (D) 1.1 m). ATW1 was filled with expanded clay aggregates (ECA) (ArgexTM 8-
132 
16 mm, porosity 35%) [27,48] and a standing water layer was kept 10 cm below surface. An 
133 
intermittent aeration regime of  2h on and 2h off was maintained with the blower at an air flow of 162 
134 
L min-1 to promote full nitrification of the wastewater.  
135 
Effluent from ATW1 then flowed gravitationally through a series of SF TWs (SF1 - 3) [49]. The 
136 
dimensions of the SFs were determined to reach nitrate (NO3-) concentrations ≤ 15 mg N L-1 at water 
137 
temperatures ≥ 16 °C, using the P-k-C* model (Eq. 1) with the parameters P = 3; C* = 0 and a Ci = 85 
138 
mg N L-1 (detailed calculation in Table S 3). The areal rate constant was chosen ka,20 = 31 m yr-1 , as a 
139 
conservative to the average ka,20 of 35 m yr-1 (n = 167) calculated by Kadlec, 2019 [28] and was adjusted 
140 
for water temperature using the Arrhenius equation (Eq. 2) with a Θ = 1.1. Based on these parameters, 
141 
the surface areas of SF1, SF2, and SF3 were set at 250 m², 125 m², and 125 m², respectively. At 
142 
temperatures below 16 °C, the denitrification capacity of the SF TWs was therefore expected to be 
143 

=== PÁG 8 ===
 
8 
 
insufficient to reach the 15 mg N L-1 effluent standard. It was hypothesized that this could be 
144 
compensated for by adding an external carbon source, hence a carbon-dosing system was foreseen 
145 
after SF3. The required carbon dose was calculated to achieve a COD:N ratio of 5:1, based on the NO3- 
146 
concentration predicted at the outlet of SF3 using the P-k-C* model with provided parameters.  
147 
Each SF was filled with 0.3 m of excavated soil from the construction phase and subsequently planted 
148 
with different macrophyte species (Table 1). A monoculture of Phragmites australis was chosen in SF1. 
149 
A variety of species was used in SF2 and SF3 for enhancing biodiversity and aesthetic purposes. After 
150 
SF3, the water flowed gravitationally into a 15 m3 second buffer tank, where carbon could be dosed. 
151 
From that second buffer tank, the water was pumped using a submersible pump onto the second 
152 
aerated TW (ATW2). A T-fitting was later installed on the outlet hose of the pump which led part of 
153 
the water back to the second buffer tank in order to improve mixing of the dosed carbon. Carbon 
154 
dosing was optimized by connecting the dosing line to the T-fitting and allowing dosing only during 
155 
pump operation. ATW2 had a total volume of 40 m³ (8 m × 5 m × 1.1 m) and was filled with the same 
156 
ECA used in ATW1. The aeration regime in ATW2 was adjusted throughout the system’s operation in 
157 
order to optimize performance. Next, the water flowed gravitationally through a series of four crushed 
158 
autoclaved aerated concrete (CAAC) basins (CAAC1 – 4) to remove phosphate. The CAAC basins were 
159 
originally connected in series and later reconfigured to enable be modular coupling. Each CAAC basin 
160 
had a working volume of 10 m³ (L 4.8 m x W 2.4 m x D 1.2 m). The CAAC was a construction waste 
161 
material, crushed by a local supplier (1 – 2 mm, porosity 30%). Finally, the water flowed gravitationally 
162 
to a small inspection well and was then discharged to the local stream. 
163 
2.2 P-k-C* model 
164 
The SF TWs were sized by using the P-k-C* model. Solving the P-k-C* equation for the pollutant 
165 
concentration C is given by [24]:  
166 

=== PÁG 9 ===
 
9 
 
𝐶 = 
𝐶𝑖-𝐶*
(1+ 𝑘𝑎
𝑃𝑞)
𝑃 + 𝐶* 
Eq. 1 
Where C (mg L-1) is the pollutant concentration; Ci (mg L-1) is the inlet concentration; C* (mg L-1) the 
167 
recalcitrant pollutant concentration; ka (d-1) the areal rate constant; P (-) the apparent number of tanks 
168 
in series and q (m d-1) the hydraulic loading rate (HLR).  
169 
Biological reaction rate constants usually are temperature dependent and can be extrapolated using 
170 
the Arrhenius equation [24,36]: 
171 
𝑘 = 𝑘20𝛩𝑇-20 
Eq. 2 
Where k (d-1) is the rate constant at temperature T (°C); k20 (d-1) is the rate constant at 20 °C and Θ (-) 
172 
is the temperature correction factor. 
173 
2.3 Water balance 
174 
The hybrid TW water mass balance was described by Eq. 3. No additional water inputs or losses were 
175 
considered since all basins were appropriately isolated from the environment by means of a liner [28]. 
176 
𝑄in + 𝑃 = 𝑄𝑜𝑢𝑡 + 𝐸𝑇 
Eq. 3 
Where Qin (m³ d-1) is the inflow water; P (m³ d-1) the precipitation; Qout (m³ d-1) the discharged water 
177 
to the stream and ET (m³ d-1) the total system evapotranspiration. 
178 
Manual readings were taken from the water meters for both influent- and effluent flows from January 
179 
2023 to October 2024 in 28-day intervals, hence the water balance was reconstructed for each of these 
180 
periods. These readings further enabled to calculate the average periodical influent volume, which was 
181 
used for determining the average daily inflow. Additionally, the flow rate of pump 1, used to deliver 
182 
water from the 223 m³ buffer tank to ATW1, was calculated by averaging the 28-day periodical pumped 
183 
volume divided by the 28-day periodical pumping time. The effluent flow rate (Qout) was measured by 
184 
a water meter at the stream discharge point and represented all the water leaving the hybrid TW.  
185 

=== PÁG 10 ===
 
10 
 
The 28-day periodical precipitation volume was calculated with data from a weather station (Viaverda), 
186 
located at a 1.2 km distance, multiplied by the hybrid TW areas receiving precipitation. These TW areas 
187 
were therefore calculated for ATW1-2, SF1–3, CAAC1–2, plus 25 % additional catchment around SF1–
188 
3 [24] due to the sloped edges, totaling at 705 m².  
189 
2.4 Carbon dosing 
190 
Carbon dosing was done with a solenoid driven dosing pump connected to an intermediate bulk 
191 
container containing commercial BRENNTAPLUS VP1 (Brenntag, Germany), a mixture of sugars and 
192 
alcohols with a COD of 800 g L-1 [50]. Each dosing pulse delivered 1.04 mL of the liquid carbon source 
193 
(LCS). The daily number of pulses was calculated as function of the temperature following a linear 
194 
equation (Eq. 4). With higher temperatures, less carbon was dosed. Initially, carbon was dosed 
195 
between a water temperature of 0 and 16 °C. 
196 
𝑁 = 𝑎*𝑇 + 𝑏 
 Eq. 4 
With: N the daily number of pulses at 1.04 mL per pulse, T the average water temperature (°C) 
197 
measured by a PT100 temperature sensor (Sontec, Germany) in SF1 the day before and a and b 
198 
manually set parameters, initially determined to reach a COD:N-ratio of 5:1 for temperatures ≤ 16 °C 
199 
according to the P-k-C* model with ka,20 = 31 m yr-1 (described in 2.1 and detailed calculation given in 
200 
Table S 3 and Figure S 5). 
201 
During system operation, multiple issues affected the reliability of the carbon dosing (e.g. electronics 
202 
malfunctioning, broken temperature sensor, …). Identified malfunctions were corrected as they 
203 
occurred to restore carbon dosing functionality. After one year of operation, the carbon source was 
204 
50% diluted with tap water to reduce viscosity. Parameters a and b (Eq. 4) were consequently modified 
205 
to ensure enough carbon was being dosed. 
206 

=== PÁG 11 ===
 
11 
 
2.5 Water quality analyses 
207 
Over a period of 3.2 years, 26 grab samples were taken from in- and effluent. Influent samples were 
208 
collected from the wastewater feeding system on top of ATW1. Effluent samples were collected from 
209 
the inspection well before discharge to the local stream (Figure S 1). Concurrently, a total of 6 grab 
210 
samples were taken after each treatment unit. Samples were stored in a refrigerator (4 °C) and 
211 
analyzed within 24 h. 
212 
Water quality parameters, i.e. biochemical oxygen demand (BOD5), total suspended solids (TSS) and 
213 
volatile suspended solids (VSS) were determined according to standard methods [51]. The COD, nitrate 
214 
(NO3--N), ammonium (NH4+-N), TN and TP were analyzed with spectrophotometric test kits (Hach, USA) 
215 
according to standard methods [48,51,52]. The used test kits are listed in Table S 9. Nitrite (NO2--N), 
216 
phosphate (PO43--P) and in some cases NO3--N were analyzed with an ion chromatograph (Eco IC, 
217 
Metrohm, Switzerland) [53]. The pH and electrical conductivity (EC) were determined with calibrated 
218 
sensors (Hach, USA). The turbidity was determined with a turbidity meter with a light source and 
219 
detector placed at 90° (HI98703, Hanna Instruments, Italy) [54]. 
220 
2.6 Pesticides 
221 
Pesticides were monitored apart from the periodical water quality parameters. Samples were taken in 
222 
duplicate in the influent, effluent and after each treatment unit, during the winter period after two 
223 
years of operation (four sampling moments in total). Grab samples were taken using 1 L amber glass 
224 
bottles to limit losses via adsorption to the recipient and via photodegradation. Samples were 
225 
transported cooled and stored immediately at 4 °C before analysis or promptly frozen if analysis could 
226 
not be done within seven days. Sample preparation and LC-MS/MS analysis was done according to 
227 
[55]. The limit of detection (LOD), limit of quantification (LOQ) and recovery in floriculture wastewater 
228 
was established for fourteen pesticides: boscalid, azoxystrobin, tebuconazole, difenoconazole, 
229 
prosulfocarb, 
pirimicarb, 
metamitron, 
metribuzin, 
penconazole, 
terbuthylazine, 
desethyl-
230 
terbuthylazine, metobromuron, spinosyn A and spinosyn D (Table S 6). These pesticides were selected 
231 

=== PÁG 12 ===
 
12 
 
based on analytical considerations. A validated method for their quantification had been previously 
232 
developed, enabling reliable detection in the floriculture wastewater. In addition, a multiresidue 
233 
analysis was performed to determine the presence of 110 pesticides in the samples taken during the 
234 
first sampling (Table S 7). 
235 
2.7 Data analysis 
236 
Data processing and calculations were performed using Microsoft Office Excel (Microsoft, USA). Plots 
237 
were made using Python 3.0 [56], including the Matplotlib library [57]. Regarding pesticides, the final 
238 
concentrations were calculated using the recovery of a specific pesticide and sample volume (Table S 
239 
8). The drinking water standard for an individual pesticide (0.1 µg L-1) was used as reference for 
240 
obtained results due to lack of other applicable standards. Removal percentages were calculated for 
241 
each sampling moment separately, but are grouped across the four sampling moments to facilitate 
242 
representation.  
243 
 
 
244 

=== PÁG 13 ===
 
13 
 
3 Results and discussion 
245 
3.1 Treatment system hydrology 
246 
During the monitored period, the average wastewater flow rate to the first buffer tank was 10.6 ± 2.5 
247 
m3 d-1. Fluctuations were attributed to variable wastewater production from the company. PLC log 
248 
data showed no events indicating full buffer utilization (Table S 4), confirming that the buffer capacity 
249 
was sufficient under the observed operating conditions. Consequently, pump 1 supplied a stable and 
250 
comparable daily inflow to ATW1 throughout the monitoring period. The hydraulic loading rates (HLRs) 
251 
and residence times (HRTs) were calculated (Table 1) based on the average wastewater inflow 10.6 ± 
252 
2.5 m³ d-1. The HRT for the hybrid TW from ATW1 until discharge in the stream was 23.2 ± 2.3 d, with 
253 
the bulk of the time spent in the SFs at 18.9 ± 2.3 d (Table 1). 
254 
The 28-day period-wise water balance is presented in Figure 1, showing each term of the water balance 
255 
equation except ET (Eq. 3). Sharp peaks in Qout during periods 13 and 15, corresponding to November 
256 
and January, were absent in Qin or P. Heavy local rainfall could have caused the underestimation of P 
257 
as the weather station was located 1.2 km away. The relatively large ATW and SF TW surface areas and 
258 
relatively small areal P values make that small changes in ET values vastly influence the water balance. 
259 
Consequently, accurate ET estimation based on Qin, Qout and P was not possible since negative ET values 
260 
were obtained in several instances. Figure 1 however indicates that effluent volumes were periodically 
261 
lower than influent volumes during the summer months, a pattern attributed to ET losses. 
262 

=== PÁG 14 ===
 
14 
 
 
263 
Figure 1: Volumes of the water balance terms (Eq. 3) during each 28-day period in the hybrid TW. Influent was calculated by 
264 
pumping times of pump 1 at a constant flow rate of 168 L min-1 during each period, effluent was recorded by the effluent 
265 
water meter; precipitation (P) calculated from weather station data recorded 1.2 km away and a 705 m² catchment area and 
266 
evapotranspiration (ET) was not considered from Eq. 3. 
267 

=== PÁG 15 ===
 
15 
 
Table 1: Hybrid TW specification. HLR Qin = hydraulic loading rate originating from wastewater flow 10.6 ± 2.5 m³ d-1 (n = 22), HLR P = hydraulic loading rate originating from average precipitation 
268 
during the monitoring period (n = 22) and has a cumulative effect going down the treatment train. 
269 
Unit 
Surface 
area (m²) 
Volume 
(m³) 
Substrate 
Porosity 
(-) 
HLR Qin  
(m d-1) 
HLR P  
(m d-1) 
HRT  
(d) 
Planted vegetation 
First buffer tank 
64 
233 
- 
- 
- 
- 
- 
- 
ATW1 
20 
22 
Expanded clay 
aggregates (ECA) 
35% 
0.53 ± 0.09 
0.003 ± 0.001 0.6 ± 0.1 
Phragmites australis 
SF1 
250 
125 
Local soil 
- 
0.04 ± 0.01 
0.003 ± 0.001 11.8 ± 2.1 
P. australis 
SF2 
125 
37.5 
Local soil 
- 
0.08 ± 0.02 
0.009 ± 0.004 3.5 ± 0.6 
Filipendula 
ulmaria, 
Alisma 
plantago 
aquatica, 
Scirpus 
lacustris, Lythrum salicaria, Carex 
acutiformis, Iris pseudacorus and 
Typha angustifolia 
SF3 
125 
37.5 
Local soil 
- 
0.08 ± 0.02 
0.011 ± 0.005 3.5 ± 0.6 
Caltha palustris and Mentha 
aquatica 
LCS dosing tank 
- 
15 
- 
 
- 
- 
- 
- 
ATW2 
40 
44 
ECA 
35% 
0.27 ± 0.05 
0.047 ± 0.022 1.2 ± 0.2 
P. australis 
Each CAAC1 – 4 
10 
10 
Crushed aerated 
autoclaved 
concrete (CAAC) 
30% 
1.06 ± 0.19 
0.195 ± 0.093 0.6 ± 0.1 
- 
 
270 

=== PÁG 16 ===
 
16 
 
3.2 Treatment performance 
271 
3.2.1 Carbon and solids 
272 
Organic matter concentrations in the horticultural wastewater were low (Table 2), with BOD5 and COD 
273 
concentrations of 22 ± 16 and 51 ± 29 mg L-1, respectively. Influent COD concentrations consistently 
274 
remained below the discharge standard of 125 mg L-1, which was expected as fertilizers do not contain 
275 
carbon. In ATW1, carbon removal was observed as COD decreased to 31 ± 5 mg L-1, indicating that 
276 
approximately 20 mg L-1 of degradable carbon was removed during the aerobic treatment. While the 
277 
goal of this aerobic treatment was to enhance nitrification (3.2.2), carbon for further denitrification 
278 
was lost as a trade-off in this treatment step.  
279 
When the LCS-dosing was operational, nearly all added carbon was removed by ATW2, resulting in 
280 
effluent BOD5 and COD concentrations were 12 ± 49 and 45 ± 82 mg L-1, respectively. Exceedance of 
281 
the COD discharge standard was measured only once, on day 1083, due to clogging in ATW2 (described 
282 
in 3.2.2). A previous clogging event was also observed on day 916, but effluent COD did not exceed 
283 
discharge standards as the concentration was 82 mg L-1. This was however the highest measured COD 
284 
value to that point. The BOD was not determined on day 916 due to a measurement error. Overall, 
285 
organic matter removal in the hybrid TW was effective due to the combined operation of the two 
286 
ATWs. However, clogging in ATW2 compromised system performance and temporarily led to 
287 
exceedances of COD and BOD5 discharge standards. 
288 
The horticultural wastewater also contained low concentrations of TSS and VSS, averaging 6.3 ± 6.8 
289 
and 4.6 ± 7.2 mg L-1, respectively. Effluent concentrations were generally lower, averaging 2.6 ± 2.9 for 
290 
TSS and 1.7 ± 2.9 mg L-1 for VSS. During the clogging events on days 916 and 1083, TSS and VSS 
291 
increased up to respectively 12.2 and 11.4 mg L-1, confirming the hydraulic problems. Throughout the 
292 
entire operation, TSS remained well below the discharge standard of 60 mg L-1. 
293 
 
294 

=== PÁG 17 ===
 
17 
 
Table 2: Discharge standards, average influent and effluent concentrations, depicted as average ± standard deviation and average removal efficiency. *Removal not accounted for LCS dosing. 
295 
Parameter 
Unit 
Discharge standard 
Influent average 
Effluent average 
Removal efficiency 
pH 
- 
6.5 – 9  
6.82 ± 0.28 (n = 26 ) 
8.67 ± 0.53 (n = 25 ) 
- 
EC 
µS cm-1  
- 
904 ± 130 (n = 26 ) 
817 ± 384 (n = 25 ) 
- 
BOD5 
mg O2 L-1  
25 
22 ± 16 (n = 22 ) 
12 ± 49 (n = 22 ) 
45%* 
COD 
mg O2 L-1  
125 
51 ± 29 (n = 26 ) 
45 ± 82 (n = 25 ) 
12%* 
TSS 
mg L-1 
60 
6.3 ± 6.8 (n = 25 ) 
2.6 ± 2.9 (n = 25 ) 
58% 
VSS 
mg L-1 
- 
4.6 ± 7.2 (n = 25 ) 
1.7 ± 2.9 (n = 25 ) 
62% 
TN with LCS dosing 
mg N L-1 
15 
115.6 ± 34.7 (n = 26 ) 
12.2 ± 6.4 (n = 11 ) 
89% 
TN without LCS dosing 
mg N L-1 
15 
115.6 ± 34.7 (n = 26 ) 
48.7 ± 24.0 (n = 14) 
58% 
NO3-  
mg N L-1 
- 
64.7 ± 20.2 (n = 26 ) 
27.3 ± 22.6 (n = 25 ) 
58% 
NH4+  
mg N L-1 
- 
10.2 ± 6 (n = 26 ) 
0.3 ± 0.7 (n = 25 ) 
97% 
TP 
mg P L-1 
2 
20.6 ± 11.6 (n = 26 ) 
1.3 ± 1.6 (n = 25 ) 
72% 
Turbidity 
NTU 
- 
2.8 ± 2.7 (n = 24 ) 
1.5 ± 2.7 (n = 24 ) 
47% 
 
296 

=== PÁG 18 ===
 
18 
 
3.2.2 Nitrogen removal 
297 
3.2.2.1 Overall performance 
298 
The horticulture wastewater entering the hybrid TW mainly contained fertilizer residues, characterized 
299 
by high nutrient concentrations. The average TN influent concentration was 116 ± 35 mg N L-1 with an 
300 
average composition of 56% NO3--N, 9% NH4+-N and 1% NO2--N (Figure S 3). The remaining 34% was 
301 
assumed to be organically bound nitrogen [51]. Nitrification was the first step to remove nitrogen. 
302 
Following the first intermittent aerobic treatment in ATW1, the nitrate concentration amounted to 67 
303 
± 10 mg N L-1 (Figure 3) due to nitrification, representing 93% ± 2% of the TN. An unexpected 40% ± 
304 
20% TN removal was observed in ATW1, which is contradictory to literature. Miyazaki et al. [25] 
305 
reported poor TN removal (5% ± 13%) under an intermittent aeration regime of 90 min on, 150 min 
306 
off. However, their influent was dominated by ammonium, whereas nitrate was the primary nitrogen 
307 
form in our study. Ammonia volatilization is excluded, as the pH before and after ATW1 averaged 6.8 
308 
± 0.2 and 6.6 ± 0.4 (n = 9), respectively. At pH values below 7.5, ammonia volatilization is considered 
309 
negligible [58]. Nitrous oxide (N2O) may be produced via both incomplete nitrifier denitrification and 
310 
incomplete heterotrophic denitrification. Reported emissions from TWs in literature are limited, with 
311 
maximum values of approximately 3% of the total influent nitrogen load [59,60]. Nitrogen removal via 
312 
anammox may represent a potential pathway, as removal efficiencies of up to 80% at nitrogen loading 
313 
rates of 15 g N m-2 d-1 have been reported for experimental TWs treating carbon-limited wastewater 
314 
(BOD/TN < 0.2) [61]. However, the anammox process requires specific microbial communities and is 
315 
favored around pH 8, suggesting that the contribution in our case remains uncertain. Plant uptake 
316 
contributes to nitrogen removal, but the relative importance decreases with increasing nitrogen 
317 
loading rates [62]. Therefore, nitrogen uptake by the plants was expected to be marginal. 
318 
Next, the series of SF TWs (SF1 – 3) were designed to remove nitrate through heterotrophic 
319 
denitrification. Plant debris were expected to act as the main carbon source because the biodegradable 
320 
carbon was lacking after ATW1. Each SF removed indeed a portion of nitrate,21%; 9% and 4% for 
321 

=== PÁG 19 ===
 
19 
 
respectively SF1 – 3. Areal removal rates were also calculated as 0.61; 0.43 and 0.15 g N m-2 d-1 for SF1 
322 
– 3, respectively. However, effluent nitrate concentrations after SF3 remained high with on average 46 
323 
± 16 mg N L-1. Areal removal rates of 0.91 g N m-2 d-1 were reported by Lin et. al. [30] for a SF TW 
324 
treating groundwater with high nitrate and low carbon concentrations. The authors highlighted that 
325 
for TWs operated at HLRs ≥ 0.04 m d-1, the organic matter input rate from the vegetation was 
326 
insufficient to support further denitrification. The HLR of SF1 was 0.04 m d-1 while SF2 and SF3 
327 
exceeded this HLR threshold (Table 1), likely resulting in lower areal denitrification rates. Following this 
328 
HLR recommendation, a larger total SF area should aid in more organic carbon input from the 
329 
macrophytes for further nitrate reduction.  
330 
3.2.2.2 Carbon dosing 
331 
Carbon release from decaying plant detritus into the water phase occurs via several mechanisms, each 
332 
with distinct reaction rates. Initially, dead plant material that reaches the water phase leaches 
333 
dissolved organic carbon. Next, biofilms colonize the litter and start the breakdown of labile materials 
334 
through hydrolysis and finally breakdown of recalcitrant materials occurs [63–65]. Mass loss of plant 
335 
matter is fastest in the beginning and follows a logarithmic pattern [66], with the following hydrolysis 
336 
being temperature dependent [67]. Average half-life rates for P. australis tissues have been reported 
337 
as 179 d [64]. Consequently, the main input from carbon through plant matter is expected when dead 
338 
plant material reaches the water phase and when temperatures are higher. In colder periods such as 
339 
winter and early spring, limited leaching and slower microbial degradation likely lead to carbon 
340 
limitation, constraining denitrification potential during these times [28]. 
341 
Because of seasonality and variation in water temperatures, combined with an expensive land area in 
342 
Flanders, the SF TWs were not expected to meet TN discharge standards during colder periods. As a 
343 
low-footprint solution, supplemental dosing of the LCS was applied in the second buffer tank, located 
344 
after SF3. The dosing volume was controlled by the water temperature (°C) through the PLC using Eq. 
345 
4 with 1.04 mL pulse-1 (Figure S 5).   
346 

=== PÁG 20 ===
 
20 
 
During the start-up phase little to no LCS was dosed due to multiple site-specific technical difficulties 
347 
(Figure 2). The following problems were faced: (1) defective pump electronics; (2) LCS too viscous to 
348 
be pumped effectively and (3) poor mixing of the LCS in the second buffer tank. These problems were 
349 
resolved after 216 days by (1) reparation of the electronics; (2) 1/2 dilution of the LCS with tap water 
350 
and (3) installing a T-fitting on the pressure side of the submersible pump, with LCS dosing restricted 
351 
to moments when the pump was active, thereby improving mixing. Following these adjustments, the 
352 
LCS dosing volume was incremented to ensure sufficient denitrification (Figure S 5) after SF3. 
353 
Validation of the adjustments was however difficult, as water temperatures exceeded 16 °C (end of 
354 
May 2022) which was the cut-off temperature for LCS dosing. Effluent TN concentrations during the 
355 
summer of 2022 (T ≥ 16 °C) averaged 17 ± 13 mg N L-1, indicating there was no stable denitrification. 
356 
This was possibly due to the plants which were still developing in the system [31]. In response, the 
357 
carbon dosing cut-off temperature was increased to 18 °C on day 377 (Figure S 5), resulting in an 
358 
improved average effluent TN of 11 ± 7 mg N L-1 until May 2023. During the next period, the 
359 
temperature sensor was malfunctioning because the cable was damaged by rodents and was replaced 
360 
on day 770. On day 916 (end of April 2024) clogging of ATW2 was visible as water flowed over the 
361 
surface. The minimum recorded water temperature up until then was 5 °C, corresponding to an LCS 
362 
dose of 91 g COD m-2 d-1.  
363 

=== PÁG 21 ===
 
21 
 
 
364 
Figure 2: TN influent and effluent concentrations in function of operational time. The horizontal dashed line indicates the TN 
365 
discharge standard of 15 mg N L-1. Temperature measured by the sensor in SF1 and recorded on the PLC was plotted on the 
366 
right hand y-axis. Missing temperature readings were not plotted. The vertical shaded areas indicate when LCS was being 
367 
dosed.  
368 
Because only one half of the ATW2 surface received water enriched with LCS, clogging was a result of 
369 
the excessive carbon loading rate over the winter period [68]. Up until that time, it was noticed that 
370 
the blower in ATW2 was constantly supplying air, creating unfavorable aerobic conditions for 
371 
denitrification. From then on, the aeration regime was intentionally coupled to the pumping, with 
372 
aeration turned off during and after pumping. Additionally, an intermittent aeration (7 min resting, 23 
373 
min aeration) was programmed to promote anoxic conditions in ATW2 after pumping. Shortly after, 
374 
another technical failure of the carbon dosing pump prevented LCS being delivered in the second 
375 
buffer tank until the end of the monitoring period.  
376 
These operational issues underline the importance of the follow-up after commissioning of a new 
377 
installation combined with regular maintenance, especially when adding complexity (e.g. blower, 
378 
pumps and sensors) to the installation. When the carbon dosing was functioning properly, TN 
379 

=== PÁG 22 ===
 
22 
 
discharge standards were met (Figure 3). However, the COD load received by ATW2 during the colder 
380 
period 2023-2024 was too high at the end of that season, resulting in clogging causing overland flow 
381 
and effluent BOD5 and COD concentrations above the discharge standard. In all other cases, COD and 
382 
BOD5 treatment system effluent concentrations were below their respective discharge standard, 
383 
showing the effectiveness of ATW2 in controlling effluent carbon. These findings highlight the balance 
384 
that needs to be maintained between dosing enough carbon for denitrification while not hindering 
385 
system operation. A possible future adjustment to ensure denitrification is to partly dose the carbon 
386 
source earlier in the treatment train. For example in one of the SFs. This way, the organic load on ATW2 
387 
would also be lowered. 
388 
The process control for LCS dosing through water temperature measurement was questionable. 
389 
Decreasing water temperature does indeed negatively impact denitrification activity [69], but 
390 
measured water temperatures did not correlate with the nitrate concentrations after SF3 (Figure S 2). 
391 
It is well regarded that the COD/NO3- -ratio is essential to allow denitrification. Ratios around 2 
392 
represent the lower limit, while ratios around 4 to 5 are considered optimal [22,27,34]. Influent TN 
393 
concentrations varied throughout operation with 30% (Table 2). The SFs did not buffer these 
394 
fluctuations as nitrate concentrations in SF3 also showed a 35% variation. Varying TN influent loads 
395 
caused SF3 nitrate concentrations to fluctuate, which reduced the predictive value of water 
396 
temperature. The weak relationship was indicated by a Pearson correlation coefficient of -0.29. When 
397 
LCS dosing was functioning, the lowest calculated COD/NO3- ratio was 2.9 and the average ratio was 
398 
4.7. These conditions supported denitrification, although the control strategy for LCS dosing remained 
399 
suboptimal. More accurate control could be achieved through nitrate sensor coupled dosing, but such 
400 
sensor is expensive and requires frequent maintenance [16,25,70].   
401 
Overall, when the LCS was dosed, the TN effluent concentration averaged 12.2 ± 6.4 mg N L-1, which 
402 
met the discharge standard of 15 mg N L-1 during most sampling moments. An average TN removal 
403 
efficiency of 89% was achieved under these conditions. In contrast, when LCS was not being dosed, TN 
404 

=== PÁG 23 ===
 
23 
 
effluent concentrations averaged 48.7 ± 24.0 mg N L-1, corresponding to a removal efficiency of 58%. 
405 
The use of LCS was therefore essential for consistently meeting the TN discharge standard. 
406 
3.2.2.3 Design considerations for detritus based denitrification 
407 
The sizing of SF1-3 was performed using the P-k-C* model (Eq. 1). Using the original P-k-C* model 
408 
parameters for SF1 (see 2.1) and applying the operational conditions: 67 mg N L-1 nitrate influent; HRT 
409 
of 0.04 m d-1 and average water temperature of 8.6 °C yields a nitrate effluent concentration of 
410 
35 mg N L-1. In contrast, the measured SF1 effluent concentration was 53 mg N L-1, indicating the model 
411 
overestimated treatment performance. The areal rate constant ka,20-value was therefore recalibrated 
412 
using hybrid TW results. Data was used where nitrate concentrations after each SF were determined 
413 
on six different winter days, with an average water temperature of 9 ± 2 °C. The HLRs originating from 
414 
Qin were used (Table 1), other parameters were equal to the ones used for the original design in 2.1. 
415 
For each SF, nitrate effluent concentrations were modelled using the P-k-C* model (Eq. 1). A best fit 
416 
ka,20 of 9.2 m yr-1 was determined by minimizing the sum of squared errors between all model outputs 
417 
and measured concentrations. Kadlec [28] reported an average denitrification ka,20 of 43 m yr-1 based 
418 
on data from 88 surface flow wetlands, with 9 m yr-1 being the 10th percentile. Carbon limitation was 
419 
also identified here as the main process modifier which decreases denitrification in surface flow TWs 
420 
[28,30].  
421 
The total needed SF surface area to reach the initial design target effluent of 15 mg N L-1 after SF3 at 
422 
16 °C was recalculated with the operational values (ka,20 = 9.2 m yr-1; Qin = 10.6 m³ d-1  and Cinf = 
423 
67 mg N L-1). When sizing the three SFs equally, 334 m² per SF unit was calculated based on the 
424 
recalibrated ka,20 value. A total SF surface area of 1002 m³ was calculated meaning the current SF area 
425 
should be doubled. The corresponding HLR was then 0.0317 m d-1, which remained below the 0.04 m 
426 
d-1 threshold for denitrification from plant detritus [30]. The land cost of doubling the SF area would 
427 
result in 3000 EUR, as the average cost for agriculture land in 2020 in the province of East Flanders was 
428 
6 EUR m-2 [71]. The largest expense would be the construction of the TW (i.e. excavation, soil disposal, 
429 

=== PÁG 24 ===
 
24 
 
lining and planting) at approximately 37000 EUR (communication with vendor). To compare, the cost 
430 
of the LCS was 0.53 EUR L-1. On average, 1460 ± 186 L yr-1 is consumed based on the final dosing regime 
431 
(Figure S 5), which resulted in an annual operational cost of 770 ± 98 EUR yr-1. Based on these numbers, 
432 
a doubled SF area would result in approximately 40000 EUR additional cost, with only a return on 
433 
investment of more than 50 yr. 
434 
 
435 
Figure 3: Nitrate concentrations (mg NO3--N L-1) for influent and after each treatment unit. Two scenarios are presented: 
436 
whether the liquid carbon source dosing (LCS-dosing) was operational (n = 5) or not (n = 2). Error bars indicate standard 
437 
deviation of the measurements: influent n = 11; ATW1 n = 7; SF1 n = 3, SF2 n = 7 and SF3 n = 7. Abbreviations: ATW1 = first 
438 
aerated TW, SF1 -3 = surface flow treatment wetlands 1 until 3, LCS-dosing = second buffer tank where LCS could be dosed 
439 
and ATW2 = second aerated TW 
440 
3.2.3 Phosphorus 
441 
Orthophosphate was the dominant form of phosphorus with 81% ± 28% in the wastewater. The fate 
442 
of phosphorus throughout the hybrid TW could thus be visualized with a phosphate concentration 
443 
profile (Figure 5). The profile shows that the CAAC basins, located after ATW2 and before the final 
444 
discharge point, were necessary to reach the discharge standard of 2 mg TP L-1. When the CAAC basins 
445 

=== PÁG 25 ===
 
25 
 
were functional, the hybrid TW achieved an average 94% ± 9% TP removal. However, the TP effluent 
446 
concentration fluctuated over time due to operational changes. At the start of the hybrid TW 
447 
operation, all four CAAC basins were functional, as water flowed through in series. Effluent pH was 
448 
regularly > 9, which was above the discharge standard (Figure 4).  
449 
The floriculture company’s hydroculture system was supplied with locally harvested rainwater. As a 
450 
result, the process-, waste- and treated water exhibited low buffer capacity and were sensitive to pH 
451 
fluctuations. The CAAC is known to increase pH with phosphate removal when calcite (CaCO3) is 
452 
present in the material structure [72]. An exponential correlation (R² = 0.74) was observed between 
453 
effluent TP concentrations and effluent pH (Figure S 6). Monitoring effluent pH in this specific case 
454 
therefore offers a practical method to anticipate TP discharge exceedances. A decreasing effluent pH 
455 
may indicate that a CAAC basin is nearing its phosphate sorption capacity in this specific application.  
456 
After 284 days, piping was adjusted to bypass CAAC3 and CAAC4 to reduce the effluent pH. As such 
457 
only CAAC1 and CAAC2 were operational. From then on, effluent pH stayed consistently below 9, with 
458 
no change in TP effluent concentrations. On day 770, the TP discharge standard of 2 mg P L-1 was 
459 
reached, likely because of reactive media saturation. As a response, CAAC basins CAAC3 and CAAC4 
460 
were taken into service. An erroneous hydraulic coupling between CAAC3 and CAAC4, possibly made 
461 
during the adjustments on day 284, led to those basins being bypassed and TP effluent concentrations 
462 
> 5 mg P L-1. On day 866, both CAAC1 and CAAC2 were coupled again in series while the erroneous 
463 
hydraulic coupling between CAAC3 and CAAC4 was not repaired. From day 971 until 1111, effluent TP 
464 
concentrations were again lower than discharge standard and previous samplings, indicating that the 
465 
CAAC in CAAC1 and CAAC2 showed some regenerative capacities, similarly observed with iron-coated 
466 
sand [73]. 
467 
The phosphorus mass captured by the CAAC basins until attaining the discharge standard (i.e. on day 
468 
770) equaled 70.3 ± 26.8 kg P, calculated with the average flow of 10.6 ± 2.5 m³ d-1 and an ATW2 
469 
effluent of 9.1 ± 3.2 mg P L-1 (n = 6). All phosphorus was likely retained in CAAC1 and CAAC2, with the 
470 

=== PÁG 26 ===
 
26 
 
majority in CAAC1, as TP effluent concentrations did not change after decoupling CAAC3 and CAAC4. 
471 
Assuming that most of the phosphorus was retained in CAAC1, and with a material density of 400 kg 
472 
m-3, an adsorption capacity of 17.6 ± 6.7 g P kg-1 was calculated. Renman and Renman [38] measured 
473 
adsorbed P content in a CAAC filter from a 19-months experiment with similar inlet P concentrations. 
474 
The highest adsorbed P content was in the beginning of the filter with 39.6 g P kg-1. This is higher than 
475 
calculated in the current study, however their HRT was approximately 33 h while ours was 15 h for 
476 
each CAAC basin. Another emerging phosphate adsorbent material is iron oxide coated sand. A  
477 
laboratory column test utilizing goat farm effluent found an adsorption capacity of 13.8 g P kg-1 [37], 
478 
similar to our results. Phosphorus removal was also calculated in the ECA filled ATW2, with 34% ± 30%, 
479 
but the standard deviation on the adsorbed mass (2.3 ± 5.9 g P kg-1) was too large and indicates that 
480 
only a small portion of P could be retained here. Similarly, Khan et al. [74] calculated 0.55 and 
481 
0.64 g P kg-1 adsorption in ECA filled TWs, emphasizing ECA only had a positive effect on phosphorus 
482 
retention during start-up phase.  
483 
 
484 

=== PÁG 27 ===
 
27 
 
 
485 
Figure 4: Effluent total phosphorus (TP) concentrations and effluent pH during full system operation. Operational changes 
486 
are indicated with a vertical line. The horizontal lines show the pH discharge range between 6.5 and 9 with darker shaded 
487 
areas indicating out of range  pH-values  
488 

=== PÁG 28 ===
 
28 
 
 
489 
Figure 5: Phosphate concentrations for influent and after each treatment unit (n ≥ 5). Error bars indicate standard deviation 
490 
of 6 measurements. Abbreviations: ATW1 = first aerated TW, SF1 -3 = integrated treatment wetlands 1 until 3, LCS-dosing = 
491 
liquid carbon source dosing tank and ATW2 = second aerated TW 
492 
3.2.4 Pesticides 
493 
The multiresidue analysis showed that a mix of pesticides was present in the influent wastewater. 
494 
Prochloraz, metalaxyl, linuron, thiofanate- methyl, carbendazim, imidacloprid, propiconazole, 
495 
cyprodinil and propamocarb were present above the general LOQ of the analytical method (0.001 
496 
µg L-1) in the influent samples. Regarding the 14 selected pesticides, only metamitron, metribuzin 
497 
and metobromuron were not detected in any of the influent samples taken.  
498 
Azoxystrobin (48 ± 32 µg L-1), boscalid (0.16 ± 0.09 µg L-1) and difenoconazole (0.12 ± 0.06 µg L-1) 
499 
were present in the influent at a concentration – average of all four samplings - above 0.1 µg L-1 
500 
(Figure 6). The concentrations of these three pesticides in the effluent were effectively reduced to 
501 
1.3 ± 1.0 µg L-1 (azoxystrobin), 0.05 ± 0.02 µg L-1 (boscalid) and 0.0009 ± 0.0005 µg L-1 
502 

=== PÁG 29 ===
 
29 
 
(difenoconazole). The corresponding total removal of azoxystrobin, boscalid and difenoconazole by 
503 
the hybrid treatment wetland was 94% ± 6%, 66% ± 12%, and 98.8% ± 0.8%, respectively.  
504 
 
505 
Figure 6: The concentrations of azoxystrobin, boscalid and difenoconazole in the influent), after ATW1, after SF1, after SF2, 
506 
after SF3, after carbon dosing (C dosing), after ATW2 and after CAAC1-4, i.e. effluent, during the four sampling moments. 
507 
Error bars indicate minimum and maximum concentrations in duplicate samples. 
508 
The performance of each individual treatment unit differed considerably between these three 
509 
pesticide (Figure 6). Azoxystrobin was mainly removed by the aerated wetlands, i.e. ATW1 and 
510 
ATW2 while boscalid removal took particularly place in the SFs and ATW2. On the other hand, 
511 
difenoconazole concentrations decreased after each treatment step, excluding the carbon dosing 
512 
and CAAC1-4. Both of these treatment steps increased the concentrations of azoxystrobin, boscalid 
513 
and difenoconazole at specific sampling times. These apparently negative removal percentages 
514 
could be attributed to: (i) grab-sampling, limiting the correlation between influent and effluent 
515 
samples of each treatment step [75], (ii) the microbial transformation of conjugated metabolites to 
516 
parent compounds [76], and (iii) the desorption of pesticides from particulate matter and substrates 
517 

=== PÁG 30 ===
 
30 
 
[75]. Because the individual TW units have distinct operational conditions (substrates composition, 
518 
plants composition, aeration regime, etc.), the relation between the observed removals and 
519 
operational conditions is complicated. Therefore, future research should include the desorption of 
520 
pesticides from the substrate materials, the extraction of pesticides from different plant parts, DNA 
521 
analyses on the biofilms, the monitoring of metabolites in influent and effluent, for instance, to gain 
522 
more insight into the main removal mechanisms of the specific pesticides. 
523 
Wehbe et al. [77] already reported the potential of TWs to effectively remove pesticides from 
524 
floriculture wastewater. In their study, removal efficiencies of carbendazim up to 91.8% were 
525 
observed under saturated conditions using a two-stage VSSF TW at pilot-scale. Moreover, the 
526 
removal efficiency could be effectively increased, relative to saturated conditions, using an 
527 
unsaturated system with effluent recirculation [77] However, information on the removal of 
528 
boscalid, azoxystrobin and difenoconazole in floriculture wastewater by full-scale TW is lacking 
529 
currently. Regarding boscalid and azoxystrobin, observed results are in correspondence with 
530 
literature, focusing on smaller scale and different water types. For instance, Ignatowicz et al. [78] 
531 
reported the removal of boscalid and azoxystrobin in municipal wastewater using a lab-scale VSSF 
532 
TW – filled with sand, gravel and stones. In that study, the concentration of boscalid was reduced 
533 
from 500 µg L-1 to below 0.1 µg L-1, while effluent concentrations of azoxystrobin were 0.2 – 
534 
7.5 µg L-1 (depending on the loading rate). Other studies also reported the removal of boscalid and 
535 
azoxystrobin in various water types [79–82]. In contrast, information on difenoconazole removal by 
536 
TWs is limited to one study so far by Pavlidis et al. [83], reporting mean difenoconazole removal 
537 
percentages ranging from 33% to 65%. by different pilot-scale floating TWs.  
538 
Pesticides can be included in the environmental permit of Flemish companies at three levels: (i) the 
539 
general conditions for all companies in Flanders in surface water, (ii) sector-specific conditions 
540 
applicable to companies belonging to a specific sector, and (iii) context-specific norms applicable to 
541 
one specific company. The general conditions contain multiple pesticides, such as terbuthylazine 
542 

=== PÁG 31 ===
 
31 
 
with a limit of 0.3 µg L-1 (VLAREM II appendix 2.3.1). However, boscalid, azoxystrobin and 
543 
difenoconazole are not taken up in this list. Furthermore, none of these three pesticides is regulated 
544 
via either the sector-specific requirements or the context-specific conditions of this floriculture 
545 
company. Consequently, no reference or standards exists to assess the compliance or impact of 
546 
current discharge. The maximum concentrations of azoxystrobin, boscalid and difenoconazole in 
547 
the effluent were 2.4 ± 0.2 µg L-1, 0.063 ± 0.001 µg L-1 and 0.002 µg L-1, respectively. These observed 
548 
concentrations are well below the highest available toxicity values to aquatic organisms of these 
549 
pesticides: acute toxicity to freshwater fish of 125 µg L-1 (boscalid), 44 µg L-1 for chronic toxicity to 
550 
aquatic invertebrates (azoxystrobin), and 5.6 µg L-1 chronic toxicity to aquatic invertebrates 
551 
(difenoconazole) [84]. Consequently, the findings suggest that the effluent of floriculture company 
552 
would not adversely impact aquatic organisms, when considering a fixed standard dilution factor of 
553 
10 used for evaluating chemical exposure of surface waters via wastewater treatment discharge 
554 
[85].  
 
555 

=== PÁG 32 ===
 
32 
 
4 Conclusions and recommendations 
556 
In this study, the overall performance of a hybrid TW consisting of ATWs, SFs and CAAC basins was 
557 
evaluated for nutrient and pesticide removal. During the slightly more than 3 yr operation, the hybrid 
558 
TW removed on average 70% ± 22% TN. For water temperatures < 18 °C, it was necessary to dose 
559 
additional LCS after the SF TWs, to ensure the 15 mg TN L-1 discharge standard was reached. Despite a 
560 
total (excluding first buffer tank) HRT of 23.2 ± 2.3 d with the majority spent in the SF TWs at 18.9 ± 
561 
2.3 d, the SF TWs did not perform denitrification as initially anticipated, likely due to a lack of 
562 
bioavailable carbon. A ka,20 value of 9.2 m yr-1 was obtained by calibration of the P-k-C* model and a 
563 
Θ = 1.1, as opposed to the 31 m yr-1 original design value. When LCS was dosed, TN discharge standards 
564 
were mostly met. However, during the winter period of year 2-3, at a maximum of 91 g COD m-2 d-1, 
565 
clogging occurred in ATW2 at the end of the cold season, resulting in COD and BOD5 exceedances. A 
566 
balance needed to be found in dosing sufficient LCS without obstructing treatment performance. 
567 
Water temperature was found to not be the best fitting parameter in the process control for 
568 
denitrification through LCS dosing. However, due to water temperature being a function of seasonality, 
569 
sufficient LCS was dosed to support denitrification and reaching of the TN discharge standard. A simple 
570 
economical analysis showed that increasing the total SF area for year-round TN removal would result 
571 
in a return on investment of more than 50 yr compared to the current LCS dosing. 
572 
When the CAAC basins were functional, an average of 94% ± 9% TP was removed. During the first 
573 
months of operation, the effluent pH was > 9 due to the material properties of the CAAC material. 
574 
Consequently, two CAAC basins were decoupled and effluent pH remained within discharge range. 
575 
After 770 days of operation, the 2 mg TP L-1 discharge standard was reached and CAAC 1 was assumed 
576 
saturated at the specific loading rate. Therefore, the two decoupled basins were put in operation. A 
577 
problem in the piping between CAAC3 and CAAC4 caused these units to be bypassed. As a response all 
578 
CAAC basins were then coupled. For the next 140 d, TP was removed and the concentration was below 
579 
the discharge standard, indicating recovery of the CAAC material in CAAC1 and CAAC2 took place.  
580 

=== PÁG 33 ===
 
33 
 
Although a mixture of pesticides was detected in the influent wastewater, only azoxystrobin, boscalid 
581 
and difenoconazole exceeded a concentration of 0.1 µg L-1. High removal of these three pesticides was 
582 
found for the complete hybrid TW and for specific individual treatment units. These results highlight 
583 
that TWs could offer a sustainable solution for removal of these pesticides from floriculture 
584 
wastewater. Nonetheless, as sampling moments were limited and only planned in the winter period, 
585 
so future work should include long-term monitoring during all seasons to gain better insight in the 
586 
pesticide removal by TWs at full-scale. Effluent concentrations were thus low and suggested that 
587 
discharge would not adversely impact aquatic organisms, though ecotoxicity tests are needed to 
588 
confirm this hypothesis. This study provides one of the first long-term and detailed monitoring datasets 
589 
for a full-scale hybrid TW treating floriculture drainage water, covering carbon, nitrogen, phosphorus 
590 
and pesticides, and including process control optimization. 
591 
 
 
592 

=== PÁG 34 ===
 
34 
 
5 Acknowledgements 
593 
The authors would like to thank Christoph, Katrien, Jeroen and Bart for the technical aid at the hybrid 
594 
TW; Ann, Lies and Hanne for their assistance with lab analyses; Lukas for the material information and 
595 
Viaverda for the weather data.  
596 
 
 
597 

=== PÁG 35 ===
 
35 
 
6 References 
598 
[1] Agentschap 
Landbouw 
en 
Zeevisserij, 
Land-bouw-rap-port 
2024, 
(2024). 
599 
https://landbouwcijfers.vlaanderen.be/landbouwrapport-2024-lara (accessed January 24, 2025). 
600 
[2] Statbel, Tab A landbouwcijfers 2023, Land- en tuinbouwbedrijven | Statbel, (2023). 
601 
https://statbel.fgov.be/nl/themas/landbouw-visserij/land-en-tuinbouwbedrijven#figures 
602 
(accessed March 4, 2025). 
603 
[3] A. Richa, S. Touil, M. Fizir, V. Martinez, Recent advances and perspectives in the treatment of 
604 
hydroponic wastewater: a review, Rev. Environ. Sci. Biotechnol. 19 (2020) 945–966. 
605 
https://doi.org/10.1007/s11157-020-09555-9. 
606 
[4] M. Rufí-Salís, A. Petit-Boix, G. Villalba, D. Sanjuan-Delmás, F. Parada, M. Ercilla-Montserrat, V. 
607 
Arcas-Pilz, J. Muñoz-Liesa, J. Rieradevall, X. Gabarrell, Recirculating water and nutrients in urban 
608 
agriculture: An opportunity towards environmental sustainability and water use efficiency?, J. 
609 
Clean. Prod. 261 (2020) 121213. https://doi.org/10.1016/j.jclepro.2020.121213. 
610 
[5] E. Fathidarehnijeh, M. Nadeem, M. Cheema, R. Thomas, M. Krishnapillai, L. Galagedara, Current 
611 
perspective on nutrient solution management strategies to improve the nutrient and water use 
612 
efficiency 
in 
hydroponic 
systems, 
Can. 
J. 
Plant 
Sci. 
104 
(2024) 
88–102. 
613 
https://doi.org/10.1139/cjps-2023-0034. 
614 
[6] S. Lee, J. Lee, Beneficial bacteria and fungi in hydroponic systems: Types and characteristics of 
615 
hydroponic 
food 
production 
methods, 
Sci. 
Hortic. 
195 
(2015) 
206–215. 
616 
https://doi.org/10.1016/j.scienta.2015.09.011. 
617 
[7] A. Mielcarek, K. Kłobukowska, J. Rodziewicz, W. Janczukowicz, K.Ł. Bryszewski, Water Nutrient 
618 
Management in Soilless Plant Cultivation versus Sustainability, Sustainability 16 (2024) 152. 
619 
https://doi.org/10.3390/su16010152. 
620 
[8] J.-H. Park, S.-H. Kim, R.D. Delaune, J.-S. Cho, J.-S. Heo, Y.S. Ok, D.-C. Seo, Enhancement of nitrate 
621 
removal in constructed wetlands utilizing a combined autotrophic and heterotrophic 
622 
denitrification technology for treating hydroponic wastewater containing high nitrate and low 
623 
organic 
carbon 
concentrations, 
Agric. 
Water 
Manag. 
162 
(2015) 
1–14. 
624 
https://doi.org/10.1016/j.agwat.2015.08.001. 
625 
[9] V. Gagnon, G. Maltais-Landry, J. Puigagut, F. Chazarenc, J. Brisson, Treatment of Hydroponics 
626 
Wastewater Using Constructed Wetlands in Winter Conditions, Water. Air. Soil Pollut. 212 (2010) 
627 
483–490. https://doi.org/10.1007/s11270-010-0362-8. 
628 
[10] J.Y. Lee, A. Rahman, J. Behrens, C. Brennan, B. Ham, H.S. Kim, C.W. Nho, S.-T. Yun, H. Azam, M.J. 
629 
Kwon, Nutrient removal from hydroponic wastewater by a microbial consortium and a culture of 
630 
Paracercomonas 
saepenatans, 
New 
Biotechnol. 
41 
(2018) 
15–24. 
631 
https://doi.org/10.1016/j.nbt.2017.11.003. 
632 
[11] A. Bawiec, Efficiency of nitrogen and phosphorus compounds removal in hydroponic wastewater 
633 
treatment 
plant, 
Environ. 
Technol. 
40 
(2019) 
2062–2072. 
634 
https://doi.org/10.1080/09593330.2018.1436595. 
635 
[12] VLAREM II, Besluit van de Vlaamse Regering tot wijziging van het besluit van de Vlaamse Regering 
636 
van 6 februari 1991 houdende vaststelling van het Vlaams reglement betreffende de 
637 
milieuvergunning en van het besluit van de Vlaamse Regering van 1 juni 1995 houdende algemene 
638 
en sectorale bepalingen inzake milieuhygiëne, voor wat betreft de milieukwaliteitsnormen voor 
639 
oppervlaktewateren, waterbodems en grondwater, 2010. 
640 
[13] VRT NWS, Slechts 1 op de 3 rivieren en meren in Europa haalt de lat voor waterkwaliteit, België 
641 
heeft 
te 
veel 
pesticiden 
en 
stikstof 
in 
het 
water, 
VRTNWS 
(2024). 
642 
https://www.vrt.be/vrtnws/nl/2024/10/15/europa-krijgt-meren-en-rivieren-amper-opgekuist-
643 
slechts-1-op-de/ (accessed September 1, 2025). 
644 
[14] J. Vymazal, Thirty years of constructed wetlands for municipal wastewater treatment in the Czech 
645 
Republic, Ecol. Eng. 194 (2023) 107054. https://doi.org/10.1016/j.ecoleng.2023.107054. 
646 

=== PÁG 36 ===
 
36 
 
[15] I.G. Hatvani, M.T. Dokulil, A. Clement, The Role of Wetlands in Mitigating Impacts From Diffuse 
647 
Agricultural Loads, in: T. Mehner, K. Tockner (Eds.), Encycl. Inland Waters Second Ed., Elsevier, 
648 
Oxford, 2022: pp. 285–299. https://doi.org/10.1016/B978-0-12-819166-8.00093-1. 
649 
[16] J. Koskiaho, M. Puustinen, Suspended solids and nutrient retention in two constructed wetlands 
650 
as determined from continuous data recorded with sensors, Ecol. Eng. 137 (2019) 65–75. 
651 
https://doi.org/10.1016/j.ecoleng.2019.04.006. 
652 
[17] A.I. Stefanakis, Constructed Wetlands for Industrial Wastewater Treatment, John Wiley & Sons, 
653 
2018. 
654 
[18] T. Engida, T. Alemu, J. Wu, D. Xu, Q. Zhou, Z. Wu, Analysis of constructed wetlands technology 
655 
performance efficiency for the treatment of floriculture industry wastewater, in Ethiopia, J. Water 
656 
Process Eng. 38 (2020) 101586. https://doi.org/10.1016/j.jwpe.2020.101586. 
657 
[19] A.I. Freeman, S. Widdowson, C. Murphy, D.J. Cooper, Economic assessment of aerated constructed 
658 
treatment wetlands using whole life costing, Water Sci. Technol. 80 (2019) 75–85. 
659 
https://doi.org/10.2166/wst.2019.246. 
660 
[20] J.-H. Park, S.-H. Kim, R.D. Delaune, J.-S. Cho, J.-S. Heo, Y.S. Ok, D.-C. Seo, Enhancement of nitrate 
661 
removal in constructed wetlands utilizing a combined autotrophic and heterotrophic 
662 
denitrification technology for treating hydroponic wastewater containing high nitrate and low 
663 
organic 
carbon 
concentrations, 
Agric. 
Water 
Manag. 
162 
(2015) 
1–14. 
664 
https://doi.org/10.1016/j.agwat.2015.08.001. 
665 
[21] T. Liu, G. Liu, Y. Qiu, J. Zhou, J. Li, J. Ma, Y. Feng, A review of enhanced strategies for nitrogen 
666 
removal in constructed wetlands: from design, influencing factors to full-scale applications and 
667 
challenges, Water Res. 288 (2026) 124662. https://doi.org/10.1016/j.watres.2025.124662. 
668 
[22] A. Morvannou, S. Troesch, D. Esser, N. Forquet, A. Petitjean, P. Molle, Using one filter stage of 
669 
unsaturated/saturated vertical flow filters for nitrogen removal and footprint reduction of 
670 
constructed 
wetlands, 
Water 
Sci. 
Technol. 
76 
(2017) 
124–133. 
671 
https://doi.org/10.2166/wst.2017.115. 
672 
[23] J. Nivala, C. Murphy, A. Freeman, Recent Advances in the Application, Design, and Operations & 
673 
Maintenance 
of 
Aerated 
Treatment 
Wetlands, 
Water 
12 
(2020) 
1188. 
674 
https://doi.org/10.3390/w12041188. 
675 
[24] R.H. Kadlec, S. Wallace, Treatment Wetlands, CRC Press, 2008. 
676 
[25] C.K. Miyazaki, A. Morvannou, E. Higelin, J. Nivala, P. Molle, Aeration strategies and total nitrogen 
677 
removal in a hybrid aerated treatment wetland, Blue-Green Syst. 5 (2023) 321–335. 
678 
https://doi.org/10.2166/bgs.2023.045. 
679 
[26] J. Nivala, S. Wallace, T. Headley, K. Kassa, H. Brix, M. van Afferden, R. Müller, Oxygen transfer and 
680 
consumption in subsurface flow treatment wetlands, Ecol. Eng. 61 (2013) 544–554. 
681 
https://doi.org/10.1016/j.ecoleng.2012.08.028. 
682 
[27] H. Khan, O. Schepers, N. van Belzen, M. Martens, Cornelis.K. Groot, Dion. van Oirschot, F. Ronsse, 
683 
Diederik.P.L. Rousseau, Effect of carbon dosing on denitrification in an aerated horizontal 
684 
subsurface flow constructed wetland used for effluent polishing, Ecol. Eng. 185 (2022) 106795. 
685 
https://doi.org/10.1016/j.ecoleng.2022.106795. 
686 
[28] R.H. Kadlec, Treatment marshes for runoff and polishing, CRC Press, 2019. 
687 
[29] F. Wu, S. He, X. Gu, P. Yan, Y. Peng, S. Sun, Z. Liu, The suitable biomass carbon source for improving 
688 
nitrogen removal in surface flow constructed wetland system: Fresh vs. withered, J. Environ. 
689 
Manage. 308 (2022) 114624. https://doi.org/10.1016/j.jenvman.2022.114624. 
690 
[30] Y.-F. Lin, S.-R. Jing, D.-Y. Lee, Y.-F. Chang, K.-C. Shih, Nitrate removal from groundwater using 
691 
constructed wetlands under various hydraulic loading rates, Bioresour. Technol. 99 (2008) 7504–
692 
7513. https://doi.org/10.1016/j.biortech.2008.02.017. 
693 
[31] B.G. Meerburg, P.H. Vereijken, W. de Visser, J. Verhagen, H. Korevaar, E.P. Querner, A.T. de Blaeij, 
694 
A. van der Werf, Surface water sanitation and biomass production in a large constructed wetland 
695 
in the Netherlands, Wetl. Ecol. Manag. 18 (2010) 463–470. https://doi.org/10.1007/s11273-010-
696 
9179-x. 
697 

=== PÁG 37 ===
 
37 
 
[32] Z. Zhang, S. Echavarria, Y. Sang, G.R. Weidman, N. Napp, M.C. Reid, Real-Time Control of 
698 
Exogenous Carbon Dosing in a Denitrifying Woodchip Bioreactor Treating Agricultural Drainage, 
699 
ACS EST Eng. 4 (2024) 1433–1443. https://doi.org/10.1021/acsestengg.4c00020. 
700 
[33] A.C. Barbera, G.L. Cirelli, V. Cavallaro, I. Di Silvestro, P. Pacifici, V. Castiglione, A. Toscano, M. 
701 
Milani, Growth and biomass production of different plant species in two different constructed 
702 
wetland 
systems 
in 
Sicily, 
Desalination 
246 
(2009) 
129–136. 
703 
https://doi.org/10.1016/j.desal.2008.03.046. 
704 
[34] P. Van Aken, N. Lambert, L. Appels, Low temperature Moving Bed Bioreactor denitrification as 
705 
mitigation measure to reduce agricultural nitrate losses, Sci. Total Environ. 810 (2022) 152110. 
706 
https://doi.org/10.1016/j.scitotenv.2021.152110. 
707 
[35] M.B. Roser, G.W. Feyereisen, K.A. Spokas, D.J. Mulla, J.S. Strock, J. Gutknecht, Carbon Dosing 
708 
Increases Nitrate Removal Rates in Denitrifying Bioreactors at Low-Temperature High-Flow 
709 
Conditions, J. Environ. Qual. 47 (2018) 856–864. https://doi.org/10.2134/jeq2018.02.0082. 
710 
[36] G. Dotro, G. Langergraber, P. Molle, J. Nivala, J. Puigagut, O. Stein, M. von Sperling, Treatment 
711 
Wetlands, IWA Publishing, 2017. https://doi.org/10.2166/9781780408774. 
712 
[37] R. Zhang, L. Wang, F. Hussain Lakho, X. Yang, V. Depuydt, W. Igodt, H. Quan Le, D.P.L. Rousseau, 
713 
S. Van Hulle, Iron oxide coated sand (IOS): Scale-up analysis and full-scale application for 
714 
phosphorus removal from goat farm wastewater, Sep. Purif. Technol. 284 (2022) 120213. 
715 
https://doi.org/10.1016/j.seppur.2021.120213. 
716 
[38] G. Renman, A. Renman, Sustainable use of crushed autoclaved aerated concrete (CAAC) as a filter 
717 
medium 
in 
wastewater 
purification, 
in: 
ISCOWA 
and 
SGI, 
2012. 
718 
https://urn.kb.se/resolve?urn=urn:nbn:se:kth:diva-103423 (accessed August 12, 2025). 
719 
[39] P. Molle, S. Martin, D. Esser, S. Besnault, C. Morlay, N. Harouiya, Phosphorus removal by the use 
720 
of apatite in constructed wetlands: Design recommendations, Water Pract. Technol. 6 (2011) 
721 
wpt2011046. https://doi.org/10.2166/wpt.2011.046. 
722 
[40] P.C.G. Pereira, C.E.T. Parente, G.O. Carvalho, J.P.M. Torres, R.O. Meire, P.R. Dorneles, O. Malm, A 
723 
review on pesticides in flower production: A push to reduce human exposure and environmental 
724 
contamination, 
Environ. 
Pollut. 
289 
(2021) 
117817. 
725 
https://doi.org/10.1016/j.envpol.2021.117817. 
726 
[41] C. Campanale, C. Massarelli, D. Losacco, D. Bisaccia, M. Triozzi, V.F. Uricchio, The monitoring of 
727 
pesticides in water matrices and the analytical criticalities: A review, TrAC Trends Anal. Chem. 144 
728 
(2021) 116423. https://doi.org/10.1016/j.trac.2021.116423. 
729 
[42] I.C. Vasilachi, D.M. Asiminicesei, D.I. Fertu, M. Gavrilescu, Occurrence and Fate of Emerging 
730 
Pollutants in Water Environment and Options for Their Removal, Water 13 (2021) 181. 
731 
https://doi.org/10.3390/w13020181. 
732 
[43] T. Liu, S. Xu, S. Lu, P. Qin, B. Bi, H. Ding, Y. Liu, X. Guo, X. Liu, A review on removal of 
733 
organophosphorus pesticides in constructed wetland: Performance, mechanism and influencing 
734 
factors, 
Sci. 
Total 
Environ. 
651 
(2019) 
2247–2268. 
735 
https://doi.org/10.1016/j.scitotenv.2018.10.087. 
736 
[44] G.D. Gikas, M. Pérez-Villanueva, M. Tsioras, C. Alexoudis, G. Pérez-Rojas, M. Masís-Mora, V. 
737 
Lizano-Fallas, C.E. Rodríguez-Rodríguez, Z. Vryzas, V.A. Tsihrintzis, Low-cost approaches for the 
738 
removal of terbuthylazine from agricultural wastewater: Constructed wetlands and biopurification 
739 
system, Chem. Eng. J. 335 (2018) 647–656. https://doi.org/10.1016/j.cej.2017.11.031. 
740 
[45] P. Parlakidis, T. Mavropoulos, Z. Vryzas, G.D. Gikas, Fluopyram removal from agricultural 
741 
equipment rinsing water using HSF pilot-scale constructed wetlands, Environ. Sci. Pollut. Res. 29 
742 
(2022) 29584–29596. https://doi.org/10.1007/s11356-021-15373-5. 
743 
[46] R. Budd, A. O’geen, K.S. Goh, S. Bondarenko, J. Gan, Removal mechanisms and fate of insecticides 
744 
in 
constructed 
wetlands, 
Chemosphere 
83 
(2011) 
1581–1587. 
745 
https://doi.org/10.1016/j.chemosphere.2011.01.012. 
746 
[47] S.D. 
Wallace, 
System 
for 
removing 
pollutants 
from 
water, 
US6200469B1, 
2001. 
747 
https://patents.google.com/patent/US6200469B1/en?oq=US+6%2c200%2c469B1 
(accessed 
748 
January 24, 2025). 
749 

=== PÁG 38 ===
 
38 
 
[48] R. Zhang, X. Yang, D. Buehler, D. van Oirschot, M. Martens, S.W.H. Van Hulle, D.P.L. Rousseau, Pilot 
750 
scale demonstration of an underground biological aerated filter for rural wastewater treatment in 
751 
a 
protected 
area, 
J. 
Water 
Process 
Eng. 
64 
(2024) 
105603. 
752 
https://doi.org/10.1016/j.jwpe.2024.105603. 
753 
[49] M. Scholz, R. Harrington, P. Carroll, A. Mustafa, The Integrated Constructed Wetlands (ICW) 
754 
concept, 
Wetlands 
27 
(2007) 
337–354. 
https://doi.org/10.1672/0277-
755 
5212(2007)27%255B337:TICWIC%255D2.0.CO;2. 
756 
[50] J. Smyk, K. Ignatowicz, Removal of Nitrogen Compounds from Wastewater in SBR Reactors with 
757 
Brenntaplus VP1, J. Ecol. Eng. 19 (2018) 129–135. https://doi.org/10.12911/22998993/77280. 
758 
[51] R.B. Baird, A.D. Eaton, E.W. Rice, Standard methods for the examination of water and 
759 
wastewaters, American Public Health Association, Washington, 2017. 
760 
[52] N. Hassan, J. Lezy, D. Parmentier, S.W.H. Van Hulle, Electrocoagulation flotation as a municipal 
761 
wastewater (pre-)treatment technology: Effect of weather conditions and current density, J. 
762 
Environ. Manage. 345 (2023) 118906. https://doi.org/10.1016/j.jenvman.2023.118906. 
763 
[53] S. Gusev, F. Louage, S. Van Hulle, D.P.L. Rousseau, Smartphone-based colorimetric method for 
764 
decentralized wastewater treatment monitoring by inexperienced users, Chemom. Intell. Lab. 
765 
Syst. 246 (2024) 105087. https://doi.org/10.1016/j.chemolab.2024.105087. 
766 
[54] R. Denolf, J. Hogie, F.L. Figueira, I. Mertens, T. De Somer, D.R. D’hooge, R. Hoogenboom, S. De 
767 
Meester, Constructing and validating ternary phase diagrams as basis for polymer dissolution 
768 
recycling, J. Mol. Liq. 387 (2023) 122630. https://doi.org/10.1016/j.molliq.2023.122630. 
769 
[55] M. Houbraken, V. Habimana, D. Senaeve, E. López-Dávila, P. Spanoghe, Multi-residue 
770 
determination and ecological risk assessment of pesticides in the lakes of Rwanda, Sci. Total 
771 
Environ. 576 (2017) 888–894. https://doi.org/10.1016/j.scitotenv.2016.10.127. 
772 
[56] G. Van Rossum, F.L. Drake, Python 3 Reference Manual, CreateSpace, Scotts Valley, CA, 2009. 
773 
[57] J.D. Hunter, Matplotlib: A 2D graphics environment, Comput. Sci. Eng. 9 (2007) 90–95. 
774 
https://doi.org/10.1109/MCSE.2007.55. 
775 
[58] J. Vymazal, Removal of nutrients in various types of constructed wetlands, Sci. Total Environ. 380 
776 
(2007) 48–65. https://doi.org/10.1016/j.scitotenv.2006.09.014. 
777 
[59] D. Yao, N. Dai, X. Hu, C. Cheng, H. Xie, Z. Hu, S. Liang, J. Zhang, New insights into the effects of 
778 
wetland plants on nitrogen removal pathways in constructed wetlands with low C/N ratio 
779 
wastewater: Contribution of partial denitrification-anammox, Water Res. 243 (2023) 120277. 
780 
https://doi.org/10.1016/j.watres.2023.120277. 
781 
[60] X. Zhou, L. Jia, C. Liang, L. Feng, R. Wang, H. Wu, Simultaneous enhancement of nitrogen removal 
782 
and nitrous oxide reduction by a saturated biochar-based intermittent aeration vertical flow 
783 
constructed wetland: Effects of influent strength, Chem. Eng. J. 334 (2018) 1842–1850. 
784 
https://doi.org/10.1016/j.cej.2017.11.066. 
785 
[61] Y. Hu, X. Zhao, Y. Zhao, Achieving high-rate autotrophic nitrogen removal via Canon process in a 
786 
modified single bed tidal flow constructed wetland, Chem. Eng. J. 237 (2014) 329–335. 
787 
https://doi.org/10.1016/j.cej.2013.10.033. 
788 
[62] K. Okada, J. Vymazal, The effect of aboveground biomass harvesting on nutrients removal in a 
789 
constructed 
wetland 
treating 
municipal 
sewage, 
Ecol. 
Eng. 
190 
(2023) 
106918. 
790 
https://doi.org/10.1016/j.ecoleng.2023.106918. 
791 
[63] G.L. Godshalk, R.G. Wetzel, Decomposition of aquatic angiosperms. III. Zostera marina L. and a 
792 
conceptual model of decomposition, Aquat. Bot. 5 (1978) 329–354. https://doi.org/10.1016/0304-
793 
3770(78)90075-X. 
794 
[64] M.J. Chimney, K.C. Pietro, Decomposition of macrophyte litter in a subtropical constructed 
795 
wetland 
in 
south 
Florida 
(USA), 
Ecol. 
Eng. 
27 
(2006) 
301–321. 
796 
https://doi.org/10.1016/j.ecoleng.2006.05.016. 
797 
[65] J. Wang, L. Chu, Biological nitrate removal from water and wastewater by solid-phase 
798 
denitrification 
process, 
Biotechnol. 
Adv. 
34 
(2016) 
1103–1112. 
799 
https://doi.org/10.1016/j.biotechadv.2016.07.001. 
800 

=== PÁG 39 ===
 
39 
 
[66] S.J. Yuckin, G. Howell, C.D. Robichaud, R.C. Rooney, Phragmites australis invasion and herbicide-
801 
based control changes primary production and decomposition in a freshwater wetland, Wetl. Ecol. 
802 
Manag. 31 (2023) 73–88. https://doi.org/10.1007/s11273-022-09902-3. 
803 
[67] R. Canziani, R. Vismara, D. Basilico, L. Zinni, Nitrogen removal in fixed-bed submerged biofilters 
804 
without backwashing, Water Sci. Technol. 40 (1999) 145–152. https://doi.org/10.1016/S0273-
805 
1223(99)00496-5. 
806 
[68] Y. Ren, Q. Gong, T.C. Zhang, J. Kang, D. Liu, Wavy Subsurface Flow and Vertical Flow Constructed 
807 
Wetlands: Effects of Aeration and Wastewater Composition on Wetland Clogging, J. Environ. Eng. 
808 
141 (2015) 04015018. https://doi.org/10.1061/(ASCE)EE.1943-7870.0000948. 
809 
[69] J. Tournebize, C. Chaumont, Ü. Mander, Implications for constructed wetlands to mitigate nitrate 
810 
and pesticide pollution in agricultural drained watersheds, Ecol. Eng. 103 (2017) 415–425. 
811 
https://doi.org/10.1016/j.ecoleng.2016.02.014. 
812 
[70] R. Cáceres, E. Pol, L. Narváez, A. Puerta, O. Marfà, Web app for real-time monitoring of the 
813 
performance of constructed wetlands treating horticultural leachates, Agric. Water Manag. 183 
814 
(2017) 177–185. https://doi.org/10.1016/j.agwat.2016.09.004. 
815 
[71] Fednot, Gemiddelde prijs per hectare van een Vlaamse landbouwgrond in de lift: +2,8%, (2024). 
816 
https://www.notaris.be/nieuws-pers/detail/gemiddelde-prijs-per-hectare-van-een-vlaamse-
817 
landbouwgrond-in-de-lift-2-8 (accessed September 16, 2025). 
818 
[72] J.A. da C. Castellar, J. Formosa, J.M. Chimenos, J. Canals, M. Bosch, J.R. Rosell, H.P. da Silva, J. 
819 
Morató, H. Brix, C.A. Arias, Crushed Autoclaved Aerated Concrete (CAAC), a Potential Reactive 
820 
Filter Medium for Enhancing Phosphorus Removal in Nature-Based Solutions—Preliminary Batch 
821 
Studies, Water 11 (2019) 1442. https://doi.org/10.3390/w11071442. 
822 
[73] V. Barcala, A. Zech, L. Osté, T. Behrends, Transport-limited kinetics of phosphate retention on iron-
823 
coated sand and practical implications, J. Contam. Hydrol. 255 (2023) 104160. 
824 
https://doi.org/10.1016/j.jconhyd.2023.104160. 
825 
[74] H. Khan, Intensified constructed wetlands as part of the demi water production chain of chemical 
826 
industries, 
dissertation, 
Ghent 
University, 
2024. 
http://hdl.handle.net/1854/LU-
827 
01HW6F9BV8PCXEV1V1GY2Q4KAR (accessed September 18, 2025). 
828 
[75] M. Köck-Schulmeyer, M. Villagrasa, M. López de Alda, R. Céspedes-Sánchez, F. Ventura, D. Barceló, 
829 
Occurrence and behavior of pesticides in wastewater treatment plants and their environmental 
830 
impact, 
Sci. 
Total 
Environ. 
458–460 
(2013) 
466–476. 
831 
https://doi.org/10.1016/j.scitotenv.2013.04.010. 
832 
[76] M. Kumar, J. Ngasepam, K. Dhangar, J. Mahlknecht, S. Manna, Critical review on negative emerging 
833 
contaminant removal efficiency of wastewater treatment systems: Concept, consistency and 
834 
consequences, 
Bioresour. 
Technol. 
352 
(2022) 
127054. 
835 
https://doi.org/10.1016/j.biortech.2022.127054. 
836 
[77] S. Wehbe, F. Zewge, Y. Inagaki, W. Sievert, N.T. Uday Kumar, A. Deshpande, Performance of 
837 
carbendazim removal using constructed wetlands for the Ethiopian floriculture industry, Water 
838 
Sci. Technol. 86 (2022) 142–151. https://doi.org/10.2166/wst.2022.199. 
839 
[78] K. Ignatowicz, Removal of Pesticides from Wastewater by the Use of Constructed Wetlands, J. Ecol. 
840 
Eng. 21 (2020) 219–223. https://doi.org/10.12911/22998993/112875. 
841 
[79] M. Puchlik, J. Łozowicki, K. Ignatowicz, B. Łozowicka, Use of constructed wetlands method to 
842 
remove selected pesticides from wastewater from fruit and vegetable industry, Vol. 29 Environ. 
843 
Eng. Syst. (2016) 82. 
844 
[80] V.A. Papaevangelou, G.D. Gikas, Z. Vryzas, V.A. Tsihrintzis, Treatment of agricultural equipment 
845 
rinsing water containing a fungicide in pilot-scale horizontal subsurface flow constructed wetlands, 
846 
Ecol. Eng. 101 (2017) 193–200. https://doi.org/10.1016/j.ecoleng.2017.01.045. 
847 
[81] E. Fernández-Pascual, M. Bork, B. Hensen, J. Lange, Hydrological tracers for assessing transport 
848 
and dissipation processes of pesticides in a model constructed wetland system, Hydrol. Earth Syst. 
849 
Sci. 24 (2020) 41–60. https://doi.org/10.5194/hess-24-41-2020. 
850 

=== PÁG 40 ===
 
40 
 
[82] K. Ignatowicz, J. Łozowicki, B. Łozowicka, J. Piekarski, Treatment of Agricultural Wastewater 
851 
Containing Pesticides by Hydrophytic Method as a Preliminary Method of Water Recovery, 
852 
Energies 16 (2023) 660. https://doi.org/10.3390/en16020660. 
853 
[83] G. Pavlidis, I. Zotou, H. Karasali, A. Marousopoulou, G. Bariamis, I. Nalbantis, V.A. Tsihrintzis, 
854 
Experiments on Pilot-Scale Constructed Floating Wetlands Efficiency in Removing Agrochemicals, 
855 
Toxics 10 (2022) 790. https://doi.org/10.3390/toxics10120790. 
856 
[84] K.A. Lewis, J. Tzilivakis, D.J. Warner, A. Green, An international database for pesticide risk 
857 
assessments and management, Hum. Ecol. Risk Assess. Int. J. 22 (2016) 1050–1064. 
858 
https://doi.org/10.1080/10807039.2015.1133242. 
859 
[85] M. Link, P.C. von der Ohe, K. Voß, R.B. Schäfer, Comparison of dilution factors for German 
860 
wastewater treatment plant effluents in receiving streams to the fixed dilution factor from 
861 
chemical 
risk 
assessment, 
Sci. 
Total 
Environ. 
598 
(2017) 
805–813. 
862 
https://doi.org/10.1016/j.scitotenv.2017.04.180. 
863 
 
864 
 
 
865 

=== PÁG 41 ===
 
41 
 
7 Supporting information 
866 
7.1 Determination method pesticides 
867 
The limit of detection (LOD), limit of quantification (LOQ) and recovery of the method were determined 
868 
for the fourteen pesticides selected: azoxystrobin, boscalid, tebuconazole, difenoconazole, 
869 
prosulfocarb, 
pirimicarb, 
terbuthylazine, 
desethyl-terbuthylazine, 
metribuzin, 
penconazole, 
870 
metobromuron, metamitron, spinosyn A, and spinosyn D. In addition to this targeted determination 
871 
of pesticides, a multiresidue analysis was done to check the presence of 110 pesticides in the 
872 
wastewater. Instrument settings for both targeted and multiresidue analyses were based on  
873 
Houbraken et al., 2017 [55].  
874 
The first step of sample preparation was filtration of sampled wastewater with a Whatman filter grade 
875 
GF/D (47 mm diameter) to remove all suspended particles. Consequently, concentrations refer to 
876 
dissolved pesticides concentrations. Next, pesticides were extracted from the water samples using 
877 
solid phase extraction by pumping the filtered water through an activated SepPak C18 cartridge. This 
878 
cartridge was thus activated with 1-2 mL methanol and rinsed with 1-2 mL of HPLC grade water. 
879 
Desorption of pesticides from the cartridges was performed with 10 mL of UPLC-graded acetonitrile 
880 
(VWR). Next, the extract was evaporated at 40 °C using a rotavapor. Any remaining droplets were 
881 
further removed with pressurized air. Afterwards, the extract was redissolved in 2 mL acetonitrile:Mili 
882 
Q water (10:90) and put into an ultrasonic bath for 15 seconds. Lastly, the extract was transferred in a 
883 
2 mL vial and stored at -21 °C until LC-MS/MS analysis. The analysis itself was performed with a triple 
884 
quadrupole system with electro-spray ionization (Waters ACQUITY UPLC, Xevo TQD mass 
885 
spectrometer) following Houbraken et al., 2017 [55]. 
886 

=== PÁG 42 ===
 
42 
 
7.2 Supporting figures 
887 
 
888 
Figure S 1: Schematic of the hybrid treatment wetland (TW) system with 1) buffer tank; 2) first forced bed  aeration (ATW1); 
889 
3.1 – 3.3) surface flow (SF) treatment wetlands (TWs); 4) Liquid carbon source (LCS) buffer tank; 5) second forced bed aeration 
890 
(ATW2); 6) control well after ATW2; 7) phosphate filters; 8) control well for effluent and 9) discharge to surface water. The 
891 
green markings show the sampling points for the respective sample names. 
892 
 
893 
 
894 
 
895 

=== PÁG 43 ===
 
43 
 
 
896 
Figure S 2: SF3 nitrate effluent concentrations in function of water temperature measured by the sensor in SF1 
897 
 
898 
Figure S 3: Measured nitrogen forms in influent and effluent. 
899 
0
20
40
60
80
100
120
140
160
TN
Nitrate
Ammonium
Nitrite
Concentration (mg N L-1)
Influent
Effluent

=== PÁG 44 ===
 
44 
 
 
900 
Figure S 4: pH for in- and effluent and after every treatment unit. N = 6, except for SF1, N = 4. 
901 
 
902 
Figure S 5: Different carbon dosing settings on the PLC during the operation of the hybrid TW. 
903 
6.0
6.5
7.0
7.5
8.0
8.5
Influent
FBA1
ITW1
ITW2
ITW3
C-dosing
FBA2
Effluent
0
1000
2000
3000
4000
5000
6000
0
2
4
6
8
10
12
14
16
18
20
Daily COD mass (g)
Average water temperature day before (°C)
0
216
377
1078

=== PÁG 45 ===
 
45 
 
 
904 
Figure S 6: Hybrid TW TP effluent concentrations in function of effluent pH. An exponential trendline y = 470133e-1.57x was 
905 
fitted with an R² = 0.74 
906 
 
907 
 
908 
 
 
909 

=== PÁG 46 ===
 
46 
 
7.3 Supporting tables 
910 
Table S 1: Original design parameters used in the P-k-C* model (Eq. 1) 
911 
  
P (tanks-
in-series) 
ka,20 (m yr-1) 
Θ 
C* (mg N 
L-1)  
Cin (mg N 
L-1) 
Qin (m³ d-1) 
Area (m²) 
Design parameter 
3 
31 
1.1 
0 
85 
15 
500 
 
912 
Table S 2: Original SF TWs HLRs derived from an estimated Qin of 15 m³ d-1  
913 
TW unit 
Area (m²) 
HLR (m d-1) 
SF1 
250 
0.06 
SF2 
125 
0.12 
SF3 
125 
0.12 
 
914 
Table S 3: P-k-C* model (Eq. 1) simulation for each water temperature with original design parameters (Table S 1) and (Table 
915 
S 2). SF1 treats Cin concentrations, SF2 treats SF1 effluent and SF3 treats SF2 effluent. The grey cell indicates the design goal 
916 
to reach the TN (100% NO3-) discharge standard of 15 mg N L-1 at 16 °C 
917 
T (°C) 
ka (m d-
1) 
Ceff SF1 (mg N L-1) 
Ceff SF2 (mg N L-1) 
Ceff SF3 (mg N L-1) 
0 
0.013 
69.4 
62.5 
56.4 
1 
0.014 
68.0 
60.7 
54.2 
2 
0.015 
66.6 
58.8 
51.9 
3 
0.017 
65.0 
56.7 
49.5 
4 
0.018 
63.4 
54.6 
46.9 
5 
0.020 
61.7 
52.3 
44.3 
6 
0.022 
59.8 
49.9 
41.7 
7 
0.025 
57.9 
47.5 
38.9 
8 
0.027 
55.8 
44.9 
36.1 
9 
0.030 
53.7 
42.3 
33.3 
10 
0.033 
51.5 
39.6 
30.5 
11 
0.036 
49.2 
36.9 
27.8 
12 
0.040 
46.8 
34.2 
25.0 
13 
0.044 
44.4 
31.5 
22.3 
14 
0.048 
41.9 
28.8 
19.8 
15 
0.053 
39.3 
26.1 
17.3 
16 
0.058 
36.8 
23.5 
15.0 
17 
0.064 
34.2 
21.0 
12.8 
18 
0.070 
31.7 
18.5 
10.9 
19 
0.077 
29.1 
16.3 
9.1 
20 
0.085 
26.7 
14.1 
7.5 
 
918 

=== PÁG 47 ===
 
47 
 
Table S 4 Estimation of pumped volumes by pump 1 
919 
28-
day 
Period 
Water 
counter 
influent (m³) 
Influent 
(m³) 
Registered 
pumping 
time (s) 
Note 
registered 
pumping time 
Estimated 
pumping 
time (s) 
Qi, Estimated 
pumped volume 
(m³) 
Estimation 
remaining volume 
buffer (m³) 
Difference water counter - estimated 
pumped volume (m³) 
1 
51298 
 
 
 
 
 
16 
 
2 
51455 
157 
54722 
 
54722 
153 
16 
4 
3 
51662 
207 
72105 
 
72105 
202 
16 
5 
4 
51938 
276 
96761 
 
96761 
271 
16 
5 
5 
52163 
225 
80460 
 
80460 
225 
16 
0 
6 
52461 
298 
92080 
3 days missing 
105580 
296 
16 
2 
7 
52805 
344 
116640 
 
116640 
327 
33 
17 
8 
53174 
369 
126000 
 
126000 
353 
50 
16 
9 
53596 
422 
126000 
 
126000 
353 
119 
69 
10 
54022 
426 
126000 
 
126000 
353 
192 
73 
11 
54285 
263 
126000 
 
126000 
353 
102 
-90 
12 
54520 
235 
92340 
 
92340 
259 
16 
-24 
13 
54927 
407 
100140 
3 days missing 
113640 
318 
105 
89 
14 
55264 
337 
0 
No data 
126000 
353 
89 
-16 
15 
55499 
235 
0 
No data 
110003 
308 
16 
-73 
16 
55749 
250 
60172 15 days missing 
89286 
250 
16 
0 
17 
56035 
286 
109800 
 
109800 
307 
16 
-21 
18 
56376 
341 
114396 
 
114396 
320 
16 
21 
19 
56673 
297 
118140 
 
118140 
331 
16 
-34 
20 
56950 
277 
107054 
 
107054 
300 
16 
-23 
21 
57256 
306 
95340 
4 days missing 
113340 
317 
16 
-11 
22 
57549 
293 
0 
No data 
104643 
293 
16 
0 
23 
57839 
290 
70500 10 days missing 
103571 
290 
16 
0 
920 

=== PÁG 48 ===
 
48 
 
Table S 5: Water balance for each 28-day period calculated using Eq. 3 
921 
28-day Period 
Qin (m³) 
P (mm) 
P (m³) 
Qout (m³) 
1 
 
115 
81 
 
2 
153 
99 
69 
 
3 
202 
7 
5 
 
4 
271 
100 
71 
 
5 
225 
78 
55 
190 
6 
296 
58 
41 
197 
7 
327 
1 
0 
192 
8 
353 
47 
33 
255 
9 
353 
138 
97 
366 
10 
353 
50 
36 
374 
11 
353 
69 
48 
335 
12 
259 
128 
90 
310 
13 
318 
152 
107 
531 
14 
353 
86 
61 
354 
15 
308 
93 
66 
434 
16 
250 
83 
59 
345 
17 
307 
89 
63 
335 
18 
320 
81 
57 
354 
19 
331 
73 
52 
302 
20 
300 
90 
63 
258 
21 
317 
66 
47 
214 
22 
293 
36 
26 
202 
23 
290 
67 
47 
197 
 
922 
Table S 6: Limit of detection (LOD) and limit of quantification (LOQ) for the determined pesticides 
923 
Compound 
LOD (mg/L) 
LOQ (mg/L) 
boscalid 
0.00057 
0.00170 
spinosyn A 
0.00004 
0.00011 
spinosyn D 
0.00004 
0.00012 
prosulfocarb 
0.00020 
0.00061 
pirimicarb 
0.00008 
0.00024 
difenoconazole 
0.00005 
0.00014 
metribuzin 
0.00033 
0.00098 
azoxystrobin 
0.00097 
0.00291 
tebuconazole 
0.00015 
0.00045 
terbuthylazine 
0.00012 
0.00036 
desethyl-terbuthylazine 
0.00006 
0.00019 
penconazole 
0.00008 
0.00023 
metobromuron 
0.00091 
0.00273 
metamitron 
0.00019 
0.00056 
 
924 

=== PÁG 49 ===
 
49 
 
Table S 7: List of pesticides checked for in the multiresidue analysis 
925 
Acephate 
Cyanizine 
Hexaconazole 
Parathion 
Spirodiclofen 
Acetamiprid 
Cyflufenamid  
Hexythiazox 
Penconazole  
Spiroxamine 
Amethryn 
Cymoxanil 
Imazalil 
Pendimehtanil 
Tau fluvalinate 
Atrazine  
Cyprodinil 
Imidacloprid 
Piperonylbutoxide 
Tebuconazole 
Azoxystrobine 
Diazinon 
Indoxacarb 
Pirimicarb 
Tebufenozide 
Benalaxyl  
Difenacoum 
Iprodione 
Pirimiphos-methyl 
Tebuthiuron 
Bentazon 
Difenconazole 
Isoproturon 
Prochloraz 
Temephos 
Bitertanol 
Diflubenzuron 
Kresoxim-methyl 
Profenofos 
Terbutryn 
Boscalid 
Dimethoate 
Linuron 
Propanil 
Terbutylazine 
Butachlor 
Dimethomorph 
Malathion 
Propazine 
Terufos 
Cadusafos 
Diuron 
Metalaxyl 
Propiconazole 
Thiabendazole 
Carbaryl 
Epoxiconazole 
Metamitron 
Propoxur 
Thiacloprid 
Carbendazim 
Ethoprophos 
Metazochlor 
Prosulfocarb 
Thiametoxam 
Carbetamide 
Fenamiphos 
Methabenzthiazuron Prosulfocarb 
Thifensulfuron-methyl 
Carbofuran 
Fenbuconazole 
Methiocarb 
Pyrachlostrobine 
Thiodicarb 
Carbosulfan 
Fenoxycarb 
Methomyl 
Pyrazosulfuron-ethyl Thiofanate-methyl 
Carfentrazon-ethyl Fenpropimorf 
Methoxifenozide 
Pyridaben 
Tirazophos 
Chlorotoluron 
Fenpyroximat 
Methribuzin 
Pyrimethanil 
Triademinol 
Chlorprofam 
Flazasulfuron 
Metsulfuron-methyl 
Sethoxydim 
Triadimefon 
Chlorpyrifos 
Fluazufop-p-bu-
tyl 
Monocrotophos 
Simazine 
Trifloxystrobine 
Ciethofencarb 
Fludioxonil 
Nicosulfuron 
Spinosad a 
Triticonazole 
Clopyralid 
Flufenacet 
Oxamyl 
Spinosad d 
Zoxamide 
 
926 
Table S 8: Recoveries and standard deviations for the determined pesticides 
927 
Compound 
Recovery 
(%) 
SD 
boscalid 
68.0 
22.2 
spinosyn A 
28.3 
18.9 
spinosyn D 
12.4 
5.9 
prosulfocarb 
33.7 
6.8 
pirimicarb 
39.1 
8.9 
difenoconazole 
37.9 
11.0 
azoxystrobin  
78.2 
8.2 
tebuconazole 
64.4 
16.0 
terbuthylazine 
40.8 
5.6 
desethyl-terbuthylazine 
43.3 
10.0 
penconazole 
55.0 
12.5 
 
928 
 
929 

=== PÁG 50 ===
 
50 
 
Table S 9: measurement methods 
930 
Measuring method 
Hach PHC 101 
Hach CDC 401 
APHA 5210 B 
Hach LCK 314/1414 
APHA 2540 D 
APHA 2540 E 
Hach LCK 238/138  
Hach LCK 340/339 or ion chromatograph  
Hach LCK 303/304/305  
Hach LCK 350/349 
Light source and detector placed at 90° (HI98703 by Hanna Instruments) 
 
931 
 
932 
```

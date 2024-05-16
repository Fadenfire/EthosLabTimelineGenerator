import requests
import json
import datetime, dateutil.parser
from PIL import Image, ImageDraw, ImageFont, ImageColor
from pathlib import Path

def configureGraph(b):
	b.setTimeRange(2011, 2024)
	
	b.addItem("Vanilla Season 1", "#FFA000", "PLFD1682F2801E7ADF")
	b.addItem("Vanilla Season 2", "#2E7D32", "PLaAVDbMg_XArcet5lwcRo12Fh9JrGKydh")
	
	b.addItem("Mindcrack Season 3", "#C2185B", "PLaAVDbMg_XApzEqyJsw8z5Ysiw2J8XbNZ")
	b.addItem("Mindcrack Season 4", "#6A1B9A", "PLaAVDbMg_XAo_pe3nb45LxQFNqHSRODeB")
	b.addItem("Battle Bane", "#FFB300", "PLaOY2J77tsftTgyAEnAQ4rVff1aIJlTU9")
	
	b.addItem("Mindcrack FTB Season 1", "#0288D1", "PLaOY2J77tsftpA7XGgsBH92pU3sbTvy3p")
	b.addItem("CrackPack", "#C62828", "PLaOY2J77tsfsuni2FZDRnW5LaNxWihFhp")
	b.addItem("Mindcrack FTB Season 2", "#0288D1", "PLaOY2J77tsftnmuaMtIjttzi3tF5v5UI-")
	b.addItem("Etho's Modded Minecraft Season 1", "#2B886C", "PLaOY2J77tsfv_5zl2yULYu7_VPrb5UcPr")
	b.addItem("Etho's Modded Minecraft Season 2", "#2B886C", "PLaOY2J77tsfsdHdEIxVbW9uz_jHr54uqE")
	
	b.addItem("Mindcrack Season 5", "#283593", "PLhAQr7JXmpXtuvuikOCnD7zw4Im7Jp25g")
	
	b.addItem("TerraFirmaCraft Season 1", "#9E9D24", "PLaOY2J77tsfsfrKHV79bfsK4efq9xkkm4")
	b.addItem("TerraFirmaCraft Season 2", "#9E9D24", "PLaOY2J77tsftUkvGjQ5mZpkJBqy4kH7yD")
	b.addItem("Fly Boys", "#00ACC1", "PLaOY2J77tsfs_wwmFcqLJ3wRL-t66FBDs")
	b.addItem("Crash Landing", "#FFA000", "PLaOY2J77tsftSq39l08SiDDBefT8f7Cf3")
	b.addItem("Hermit Pack", "#F5B041", "PLaOY2J77tsfth8oNCjhfz3j3d0b_0Kqs0")
	b.addItem("Project Ozone 2", "#E74C3C", "PLaOY2J77tsfvufy6BrvCEIzslQ--tf8he")
	b.addItem("Foolcraft", "#2ECC71", "PLaOY2J77tsfutMPlHolDhmK51FhONCJ0n")
	b.addItem("TerraFirmaPunk", "#1A237E", "PLaOY2J77tsfsBIfjowtCRUwd4_zs4ZWj2")
	b.addItem("Pixelmon", "#CF0000", "PLaOY2J77tsfs4IkNkYyh7aEFHMmwJ7QoU")
	b.addItem("Pixelmon 2", "#CF0000", "PLaOY2J77tsfsW-hsCJJiSG1DbgGu8wdN5")
	b.addItem("Enigmatica 2", "#A8CA2E", "PLaOY2J77tsfv-Drp9u3qXCTw1edMMA_Wr")
	b.addItem("Vault Hunters", "#A8CA2E", "PLaOY2J77tsfsuH4eepqDOkgUjnx3VPTeN")
	
	b.addItem("HermitCraft Season 3", "#9575CD", "PLaOY2J77tsftImkOhqT2iENxDY8racne0")
	b.addItem("HermitCraft Season 4", "#9575CD", "PLaOY2J77tsfv7BX0BvLQwx0TosGJOwYGW")
	b.addItem("HermitCraft Season 5", "#9575CD", "PLaOY2J77tsft6W8QGp34ED0D_JIwWAa_5")
	b.addItem("HermitCraft Season 7", "#9575CD", "PLaOY2J77tsfsGfJp92z_a0qGH5HumWKbt")
	b.addItem("HermitCraft Season 8", "#9575CD", "PLaOY2J77tsfs27MmQV9dTaZ0TANvLBYPs")
	b.addItem("HermitCraft Season 9", "#9575CD", "PLaOY2J77tsftRyFOkLSlYmK164yTcPLQH")
	b.addItem("HermitCraft Season 10", "#9575CD", "PLaOY2J77tsfsi2FfpVH9R1nKC5KH_KjeB")
	
	b.addItem("Terraria 1.0", "#228B22", "PLaOY2J77tsfvwBjgWnlZJI-Ri1vboLQAJ")
	b.addItem("Terraria 1.2", "#228B22", "PLaOY2J77tsfsycFNjlLnxnB5iWy-vJaa_")
	b.addItem("ARK: Survival Evolved", "#db5420", "PLaOY2J77tsful6PqNh4sbupsWkoa-IhKe")
	b.addItem("Terraria 1.3", "#228B22", "PLaOY2J77tsfummhIn_P47uEVI52JvxiGo")
	
	b.addItem("Ruins of the Mindcrackers", "#8b4367", "PLaOY2J77tsfv1MDrqHhuazr9HRUWAYdNJ")
	b.addItem("Ruins of the Mindcrackers 2", "#543864", "PLaOY2J77tsft4GuXDzqqaG3UnnJIrwigu")
	b.addItem("Uncharted Territory 3", "#5ac18e", "PLaOY2J77tsfsDZ5IgqXgj8tK_diAnFiKk")
	b.addItem("Simulation Protocol", "#ffa500", "PLaOY2J77tsftOSVCfL2WfNC_SjF_ldOHE")
	b.addItem("Sky Factory 2.5", "#3399ff", "PLaOY2J77tsftlooXyzhYjT8Ec__ec4sMn")
	b.addItem("Terra Restore 2", "#00838F", "PLaOY2J77tsftxiBJGdzsU_9iNizTG1FzV")
	b.addItem("Labyrinth of Puzzles", "#ff7373", "PLaOY2J77tsfueAIwwx4VIGyzcVXzlE0kB")
	b.addItem("Don't Starve - Team Canada", "#795548", "PLaOY2J77tsfty3ncnO5Uvn9mJCdKmxT40")
	b.addItem("Captive Minecraft 4", "#66cccc", "PLaOY2J77tsft-3Y42fTRx_n-3KbsKaqRv")
	b.addItem("ARK Ragnarok", "#db5420", "PLaOY2J77tsfsf0FABKtgSa5OVgqS7Hk1J")
	b.addItem("Diversity 3", "#45B39D", "PLaOY2J77tsfuNtwn0UUFp4_kNgbWkbtHY")
	b.addItem("R.A.D. Pack", "#117094", "PLaOY2J77tsft8qj_gzBcPL6zYHYP0P9Gw")
	
	b.addItem("OOGE Spellbound Caves", "#0D47A1", "PLaOY2J77tsftshTiVAUxsHawAqjj_h4u3")
	b.addItem("OOGE Kaizo Caverns", "#FF5722", "PLaOY2J77tsfu82G0MF4gXvcToTwuUdWQ5")
	b.addItem("OOGE Vinyl Fantasy II", "#004D40", "PLaOY2J77tsfvmm-f4ptiJApdv554KOfsW")
	
	b.addItem("Spellbound Caves Rush", "#0D47A1", "PLaOY2J77tsft2LTFJ7-jX6riihEZRdALR")
	b.addItem("No Man's Sky", "#F39C12", "PLaOY2J77tsfvLL3iLoSRJflpbUdUIYED-")
	b.addItem("Uncharted Territory 2", "#5ac18e", "PLaOY2J77tsfsvPtC60EvhZIZta0px0gka")
	b.addItem("Uncharted Territory", "#5ac18e", "PLaOY2J77tsftLS7ERhbT1djaHqeC_nVlm")
	b.addItem("Super Hostile - Canopy Carnage", "#43A047", "PLaOY2J77tsfvITch3Mdbfc9P18FAary8U")
	b.addItem("Super Hostile - Legendary", "#D32F2F", "PLaOY2J77tsftUyr2KfrDmiOSWFAKcNjrD")
	
	b.addItem("Harvest Moon 64", "#C0392B", "PLaOY2J77tsfsLR0njKkY_t8KKGNmLlQbO")
	b.addItem("Day of the Tentacle", "#2980B9", "PLaOY2J77tsftxg5f0UZfH-L5V9uq4ly3N")
	b.addItem("SOTS The Pit", "#2980B9", "PLaOY2J77tsfuCk7bZPw1UQooVzLczTQRp")
	b.addItem("Cubeworld", "#2ECC71", "PLaOY2J77tsfs93IRQepYFymB_FHUmOZrL")
	b.addItem("Starbound Early Access", "#EC407A", "PLaOY2J77tsfsxTUv7C4UOJANrwy9i5fxu")
	b.addItem("Pixel Piracy", "#922B21", "PLaOY2J77tsfuwa3b6lwuVS15OahwXuqmQ")
	b.addItem("Starbound", "#EC407A", "PLaOY2J77tsftUlXVo6E3I_T7uceluy-MK")
	b.addItem("Sam & Max", "#EF5350", "PLaOY2J77tsfs5_OiaI-NPjtgmC2c-50qr")
	b.addItem("Don't Starve - Docm77", "#795548", "PLaOY2J77tsfsxVgPlC2RXtvWFw2MtpRuE")
	b.addItem("Don't Starve", "#795548", "PLaOY2J77tsfsDbqCFvWx78qSWObD4mnYT")
	
	b.addItem("Planetary Confinement", "#C62828", "PLaOY2J77tsfsmMzK7KPi-OHNWnlJlF_Ri")
	b.addItem("ARK PvP", "#db5420", "PLaOY2J77tsfvFXn288CUYwPSgPqplNQfm")
	b.addItem("Unturned", "#2980B9", "PLaOY2J77tsfsgzHesirZYGYkOYpB_nyb-")
	
	b.addItem("Survival of the Fittest 1", "#546E7A", "PLaOY2J77tsfsZmlaF4SUr-JayskEdnTIj")
	b.addItem("Survival of the Fittest 2", "#546E7A", "PLaOY2J77tsftOEyJl0RdvIAxSaiSbArAw")
	b.addItem("HermitCraft UHC 9", "#546E7A", "PLaOY2J77tsfs2fpXt5E9bG6-Pzl8kk2Tz")
	b.addItem("Hermit Wars", "#546E7A", "PLaOY2J77tsfsQuhwE6OUWVXmNlH7b4INC")
	b.addItem("Hermit Quest Season 1", "#546E7A", "PLaOY2J77tsft4-CYWI1Vs1WTubpM8NAF4")
	b.addItem("Hermit Quest Season 2", "#546E7A", "PLaOY2J77tsfuUPp7cbBuCSretHSHP08vo")
	b.addItem("Hardcore Hermits", "#424242", "PLaOY2J77tsfvGPG8Bpo10AeiCbEN8nguh")
	b.addItem("PvP - Nail", "#1A237E", "PLaOY2J77tsfsHMsjKNHr-B_E7HxkKl-1V") #??
	
	b.addItem("3rd Life", "#D32F2F", "PLaOY2J77tsfuMKQoh1B5q1MNMPNer6n98")
	b.addItem("Last Life", "#D32F2F", "PLaOY2J77tsfttRJ0MlpCazoS03hWAH4nN")
	b.addItem("Double Life", "#D32F2F", "PLaOY2J77tsftvd3tQDITU3kPPh-6-9rFR")
	b.addItem("Limited Life", "#D32F2F", "PLaOY2J77tsft-JinZSd7kYEZtlh8Z_xu2")
	b.addItem("Secret Life", "#D32F2F", "PLaOY2J77tsfvzu69_Td8wdycdJbJmqBCN")
	
	# Smaller series
	b.addItem("Mindcrack UHC 3", "#546E7a", "PLaOY2J77tsfuL_Mw3wuApuCLI1BiR0q1k")
	b.addItem("Mindcrack UHC 4", "#546E7a", "PLaOY2J77tsfusgJag9iYZT-PEUb_3PUep", "PLaOY2J77tsftpEc6JbmraYDVOJJQ19v40")
	b.addItem("Mindcrack UHC 5", "#546E7a", "PLaOY2J77tsfvxSWX_vISBacsYkljfMTH9")
	b.addItem("Mindcrack UHC 6", "#546E7a", "PLaOY2J77tsfuiP_X59RPyAJMTsPaVrG0F")
	b.addItem("Mindcrack UHC 8", "#546E7a", "PLaOY2J77tsfunfbUVVWajF3zm7tUG12LS")
	b.addItem("Mindcrack UHC 9", "#546E7a", "PLaOY2J77tsfuk0T-V2GDA6YSTPg-q06Vs")
	b.addItem("Mindcrack UHC 10", "#546E7a", "PLaOY2J77tsfuyLi-nyJWeWz4JAMJ8FfTS")
	b.addItem("Mindcrack UHC 11", "#546E7a", "PLaOY2J77tsfupWCxsK5ZOqAy_eNqLphUW")
	b.addItem("Mindcrack UHC 13", "#546E7a", "PLaOY2J77tsfuFGNiZE6QevgQHgcGeQDvY")
	b.addItem("Mindcrack UHC 14", "#546E7a", "PLaOY2J77tsfvqeK9x7lui2acHRszyC1Mw")
	b.addItem("Mindcrack UHC 15", "#546E7a", "PLaOY2J77tsftiUKxYl6RTKKtQnF49ikMm")
	b.addItem("Mindcrack UHC 16", "#546E7a", "PLaOY2J77tsfsCzaySrj7dN8e7Gn4qiUlf")
	
	b.addItem("PvP - Calamity", "#1A237E", "PLaOY2J77tsfsFi80iCfhAt3iz77pwcSOf")
	b.addItem("PvP - Cluster Chunk", "#1A237E", "PLaOY2J77tsft5r3Wkss9N-YtTJaVUgNBW")
	b.addItem("PvP - Revolution", "#1A237E", "PLaOY2J77tsfs_G-NQKrMEFyYKKhuY616o")
	
	b.addItem("TNT Olympics", "#424242", "PLaOY2J77tsfuZKb23xGKhTmDURa8FxxNs")
	b.addItem("PlayMindCrack", "#546E7A", "PLaOY2J77tsftHwZ_eY2O5PES6hrmAMKq-")
	b.addItem("Drobnovian Knights", "#424242", "PLaOY2J77tsfvQDLJOFzmyZkY0iWxg38rc")

def main():
	global googleApiKey
	
	scriptDir = Path(__file__).resolve().parent
	cacheFile = scriptDir / "cache.json"
	googleApiKey = scriptDir.joinpath("google_api_key.txt").read_text().strip()
	
	builder = GraphBuilder(cacheFile)
	
	configureGraph(builder)
	drawGraph(scriptDir, builder)
	
	builder.writeCache()

def drawGraph(scriptDir, builder):
	fontFile = str(scriptDir / "Roboto-Bold.ttf")
	fontSmall = ImageFont.truetype(fontFile, 24)
	fontNormal = ImageFont.truetype(fontFile, 32)
	
	timelineStart = builder.startTime
	timelineEnd = builder.endTime
	
	backgroundColor = ImageColor.getrgb("#EEEEEF")
	timelineColor = ImageColor.getrgb("#ABABAB")
	darkLabelColor = ImageColor.getrgb("#888888")
	yearScale = 730 #Number of pixels in a year
	xMargin = 50
	yMargin = 50
	timelineWidth = (timelineEnd - timelineStart).days * yearScale // 365
	timelineHeight = 24
	barHeight = 30
	barPadding = 10
	rowHeight = barPadding + barHeight
	
	rowCount = builder.findBounds(yearScale, fontSmall)
	imageWidth = xMargin * 2 + timelineWidth
	imageHeight = yMargin * 2 + timelineHeight + rowCount * rowHeight
	
	image = Image.new("RGB", (imageWidth, imageHeight), backgroundColor)
	draw = ImageDraw.Draw(image)
	
	def drawRectangle(x, y, width, height, color):
		draw.rectangle([x, y, x + width, y + height], color)
	
	#Draw timeline
	drawRectangle(xMargin, yMargin + timelineHeight // 2 - 2, timelineWidth, 4, timelineColor)
	
	date = timelineStart
	for year in range(timelineStart.year, timelineEnd.year + 1):
		for month in range(1, 13):
			date = datetime.date(year, month, 1)
			yearX = xMargin + (date - timelineStart).days * yearScale // 365
			
			if date.month == 1:
				drawRectangle(yearX - 2, yMargin, 4, timelineHeight, timelineColor)
				draw.text([yearX - fontNormal.getlength(str(year)) // 2, yMargin - 10 - 32], str(year), timelineColor, fontNormal)
				
				if date.year == timelineEnd.year: break
			else:
				drawRectangle(yearX - 1, yMargin + timelineHeight // 4, 2, timelineHeight // 2, timelineColor)
	
	singleDayWidth = yearScale // 365
	
	for item in builder.items:
		x = xMargin + item.barStartX
		y = yMargin + timelineHeight + item.rowIndex * rowHeight + barPadding
		
		drawRectangle(x, y, item.barWidth, barHeight, item.color)
		
		for time in item.videoTimes:
			drawRectangle(x + (time - item.startTime).days * yearScale // 365, y, singleDayWidth, barHeight, item.lightColor)
		
		if item.isInside:
			draw.text([x + item.barWidth / 2 - item.labelWidth / 2, y], item.name, backgroundColor, fontSmall)
		else:
			draw.text([x + item.barWidth + 5, y], item.name, darkLabelColor, fontSmall)
	
	sig = "Made by /u/Silly511"
	draw.text([imageWidth - 5 - fontNormal.getlength(sig), imageHeight - 40], sig, timelineColor, fontNormal)
	
	image.save("graph.png", "PNG")

class GraphItem:
	def __init__(self, name, color, videoTimes):
		self.name = name
		self.color = ImageColor.getrgb(color)
		self.lightColor = tuple([min(255, x + 12) for x in self.color])
		self.videoTimes = videoTimes
		self.startTime = min(videoTimes)
		self.endTime = max(videoTimes)
	
	def findBounds(self, timelineStart, yearScale, font):
		self.barStartX = (self.startTime - timelineStart).days * yearScale / 365
		self.barEndX = (self.endTime - timelineStart).days * yearScale / 365
		self.labelWidth = font.getlength(self.name) #Width of the label text
		self.barWidth = self.barEndX - self.barStartX
		self.isInside = (self.labelWidth + 6) < self.barWidth #If the label text is small enough to fit inside the bar
		self.totalEndX = self.barEndX if self.isInside else self.barEndX + 8 + self.labelWidth #X coord of the end of the bar including label
	
	def intersectsWith(self, other):
		return not ((self.barStartX < other.barStartX and self.totalEndX < other.barStartX) or (self.barStartX > other.totalEndX and self.totalEndX > other.totalEndX))

class GraphBuilder:
	def __init__(self, cacheFile):
		self.cacheFile = cacheFile
		self.cache = json.loads(cacheFile.read_text()) if cacheFile.is_file() else dict()
		self.http = requests.Session()
		self.items = list()
		
		self.http.headers.update({"Accept": "application/json"})
	
	def findBounds(self, yearScale, font):
		itemsPerRow = list()
		
		for currentItem in self.items:
			currentItem.findBounds(self.startTime, yearScale, font)
			
			for i, row in enumerate(itemsPerRow):
				for item in row:
					if currentItem.intersectsWith(item):
						break
					else:
						continue
				else:
					currentItem.rowIndex = i
					row.append(currentItem)
					break
			else:
				newRow = [currentItem]
				currentItem.rowIndex = len(itemsPerRow)
				itemsPerRow.append(newRow)
		
		return len(itemsPerRow)
	
	def setTimeRange(self, startYear, endYear):
		self.startTime = datetime.date(startYear, 1, 1)
		self.endTime = datetime.date(endYear + 1, 1, 1)
	
	def addItem(self, name, color, *playlistIds):
		timesList = list()
		
		for playlistId in playlistIds:
			timesList += getPlaylistTimes(self.http, self.cache, playlistId)
		
		self.items.append(GraphItem(name, color, timesList))
	
	def writeCache(self):
		self.cacheFile.write_text(json.dumps(self.cache, indent="\t"))

def getPlaylistTimes(http, playlistCache, playlistId):
	if playlistId in playlistCache:
		return [datetime.date.fromordinal(time) for time in playlistCache[playlistId]]
	else:
		print(f"Downloading playlist {playlistId}")
		params = {"part": "contentDetails", "fields": "nextPageToken,items/contentDetails/videoPublishedAt", "maxResults": "50", "playlistId": playlistId, "key": googleApiKey}
		timesList = list()
		
		while True:
			res = http.get("https://www.googleapis.com/youtube/v3/playlistItems", params=params).json()
			timesList += [dateutil.parser.isoparse(vid["contentDetails"]["videoPublishedAt"]).date() for vid in res["items"]]
			
			if "nextPageToken" in res:
				params["pageToken"] = res["nextPageToken"]
			else:
				break
		
		playlistCache[playlistId] = [time.toordinal() for time in timesList]
		return timesList

main()
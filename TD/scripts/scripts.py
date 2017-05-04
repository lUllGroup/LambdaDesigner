classes = {
  'chopToTop' : (choptoTOP, 'chopto', 'TOP'),
  'circleTop' : (circleTOP, 'circle', 'TOP'),
  'compositeTop' : (compositeTOP, 'comp', 'TOP'),
  'displace' : (displaceTOP, 'displace', 'TOP'),
  'feedbackTop' : (feedbackTOP, 'feedback', 'TOP'),
  'movieFileIn' : (moviefileinTOP, 'moviefilein', 'TOP'),
  'inTop' : (inTOP, 'in', 'TOP'),
  'nullTop' : (outTOP, 'null', 'TOP'),
  'outTop' : (outTOP, 'out', 'TOP'),
  'render' : (renderTOP, 'render', 'TOP'),
  'levelTop' : (levelTOP, 'level', 'TOP'),
  'transform' : (transformTOP, 'transform', 'TOP'),
  'noiseTop' : (noiseTOP, 'noise', 'TOP'),
  'ramp' : (rampTOP, 'ramp', 'TOP'),
  'switchTop' : (switchTOP, 'switch', 'TOP'),
  'selectTop' : (selectTOP, 'select', 'TOP'),

  'audioIn' : (audiodeviceinCHOP, 'audiodevicein', 'CHOP'),
  'audioSpectrum' : (audiospectrumCHOP, 'audiospect', 'CHOP'),
  'constantChop' : (constantCHOP, 'constant', 'CHOP'),
  'count' : (countCHOP, 'count', 'CHOP'),
  'delay' : (delayCHOP, 'delay', 'CHOP'),
  'fan' : (fanCHOP, 'fan', 'CHOP'),
  'feedbackChop' : (feedbackCHOP, 'feedback', 'CHOP'),
  'hold' : (holdCHOP, 'hold', 'CHOP'),
  'logic' : (logicCHOP, 'logic', 'CHOP'),
  'inChop' : (inCHOP, 'in', 'CHOP'),
  'math' : (mathCHOP, 'math', 'CHOP'),
  'mergeChop' : (mergeCHOP, 'merge', 'CHOP'),
  'outChop' : (outCHOP, 'out', 'CHOP'),
  'noiseChop' : (noiseCHOP, 'noise', 'CHOP'),
  'sopToChop' : (soptoCHOP, 'sopto', 'CHOP'),
  'selectChop' : (selectCHOP, 'select', 'CHOP'),
  'switchChop' : (switchCHOP, 'switch', 'CHOP'),
  'timer' : (timerCHOP, 'timer', 'CHOP'),

  'chopToSop' : (choptoSOP, 'chopto', 'SOP'),
  'circleSop' : (circleSOP, 'circle', 'SOP'),
  'noiseSop' : (noiseSOP, 'noise', 'SOP'),
  'inSop' : (inSOP, 'in', 'SOP'),
  'outSop' : (outSOP, 'out', 'SOP'),
  'sphere' : (sphereSOP, 'sphere', 'SOP'),

  'inMat' : (inMAT, 'in', 'MAT'),
  'outMat' : (outMAT, 'out', 'MAT'),
  'constMat' : (constantMAT, 'constant', 'MAT'),

  'chopExec' : (chopexecuteDAT, 'chopexecute', 'DAT'),
  'datExec' : (datexecuteDAT, 'datexecute', 'DAT'),
  'inDat' : (inDAT, 'in', 'DAT'),
  'outDat' : (outDAT, 'out', 'DAT'),
  'selectDat' : (selectDAT, 'select', 'DAT'),
  'table' : (tableDAT, 'table', 'DAT'),
  'textDat' : (textDAT, 'text', 'DAT'),
  'tcpip' : (tcpipDAT, 'tcpip', 'DAT'),

  'camera' : (cameraCOMP, 'cam', 'COMP'),
  'geo' : (geometryCOMP, 'geo', 'COMP'),
  'light' : (lightCOMP, 'light', 'COMP'),
  'base' : (baseCOMP, 'base', 'COMP')
}

def getClass(opname, default):
  return classes.get(opname, default)

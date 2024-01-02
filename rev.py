import clr
import sys
clr.AddReference('RevitServices')
clr.AddReference("RevitNodes")
clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")
import RevitServices
from Autodesk.Revit.DB import *
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *

doc = DocumentManager.Instance.CurrentDBDocument
app = DocumentManager.Instance.CurrentUIApplication.Application
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application 

elements = IN[0]
parameter =  IN[1]

outlist = []
familyType = []

for i in UnwrapElement(elements):
    for j in i.Parameters:
        if j.isShared and j.Definition.Name == parameter :
            parameterValue = i.get_parameter(j.GUID)
            outlist.append(parameterValue.AsString())
for i in UnwrapElement(IN[0]):
    id = i.GetTypeId()
    if id == ElementId.InvalidElementId:
        familyType.append(None)
    else:
        familyType.append(doc.GetElement(id))

buitparam = BuiltInParameter.ALL_MODEL_TYPE_MARK 

for i in UnwrapElement(familyType):
    typemark = i.get_parameter(buitparam)
    outlist.append(typemark.AsString())
OUT = outlist


# -------------------------------------------------------------------------------
# Copyright IBM Corp. 2016
# 
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -------------------------------------------------------------------------------

from pixiedust.display.display import *
from pixiedust.display import *
from .codeGenerator import PixieDustCodeGenDisplay

codegenArgs = []
defaultCodeGenSource = 'https://ibm-cds-labs.github.io/pixiedust_incubator/codegen/codegen-default.json'

class PixieDustCodeGenPluginMeta(DisplayHandlerMeta):
    @addId
    def getMenuInfo(self,entity):
        if entity==self.__class__:
            return [
                {"id": "codeGen"}
            ]
        else:
            return []
    def newDisplayHandler(self,options,entity):
        options['codeGenArgs'] = codegenArgs
        return PixieDustCodeGenDisplay(options,entity)

registerDisplayHandler(PixieDustCodeGenPluginMeta())

def codeGenerator(*args):
    global codegenArgs
    if args:
        codegenArgs = list(args)
    else:
        codegenArgs = [defaultCodeGenSource]
    display(PixieDustCodeGenPluginMeta)
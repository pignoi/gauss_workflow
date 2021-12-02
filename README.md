# gauss_workflow
relate the gaussian calculate software with workflow to make the work more convenient.

# readfile
主要功能是读取用户输入的结构文件信息，然后再形成计算文件输出，目前想到的是xyz结构文件，gjf文件

# userin
控制用户的输入，主要工作是收集用户的输入信息以及将其整合到class中，其中json文件为规定计算所使用计算机资源的文件，或许可以考虑将计算所使用的计算条件也一并整合到其中

# main
程序的主要程序，将各个组件整合起来，未来将要和workflow整合在一起，形成更加完善的工作流
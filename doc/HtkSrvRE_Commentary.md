# Hieratika Server Reverse Engineered Commentary.

Expected life of this document short : a means to an end and to start getting feedback on what I grok and what I don't.

Methodology : starting from hieratika/servers/psps/pspsserver a quick look through the code.  Some thoughts.

# Top Level Operation

The main agents are a web server (hieratika server) which adapts itself to a plant system server to provide a viewer and editor for the configuration data associated with the plant system.   The system is modelled as a tree.  Leaf nodes have values which can be live (readback) or set (write to).  Values to write can come from a schedule (specific source) or a library (reference source).   Overall the pattern is somewhat model/view/controller and the look and feel are well separated from the model.   The design is aiming for clean separation of concerns, and so although the immediate implementation assumes an HTML view, this will be abstracted.  Likewise, the system is designed to flexibly handle alternative data sources as long as they conform to a tree structured hierarchical object.

For the PSPS plant system, particular data is serialised to file in XML format, and this can be loaded into in-memory python representations which are then operated upon via interaction with the user through the web interface (or REST API?).

1. Server is initialised from a .ini file which contains key/value settings in three main stanzas:
..1. hieratika web server setup : location of html; definition of the server class; broadcast IP + port ; syntax marker
..1. plant system server configuration : base directory, locks, xmlId accelerators and cache settings, autocreation flag, links to permissions
..1. authenication information and group definition

## Server Class API Overview

A server provides a extract/transform/load service to a plant system.   The initial setup is introspective. i.e. Passed a valid XML entry point, the XML tree is walked and an HTML interface emitted in response.   It appears that large elements of the way that the html logic is implemented lie outside the pspserver.py code in the html5 markup.   The server API then responds.

Considerable care has been taken to make the system robust for parallel operations, using the multiprocessing locks to protect critical code regions.

To understand the data/work flows my approach is build out a glossary of the nouns/atrtributes/verbs and then develop a diagram to show expected routes through the code.

### Nouns

1. Variable
1. AbsoluteVariable
1. Constraint
1. Page
1. Library
1. Transformation
1. Schedule
1. CachedXmlTree
1. Plant

### Verbs

1. get
1. getAll
1. update
1. save
1. load
1. attach
1. find
1. create
1. convert

## Questions to Andre et al.

1. PSPS represents plant systems as XML with a fairly firmly controlled scheda/validation.   JET systems are modelled in configuration using CCL which is syntactic sugar to provide RDF databases.   The RDF/semantic web model is more fluid, and this makes it amenable to some flexible annotation styles which are reminiscent of the advantages of MARTe .cfg syntax in which defining user specified properties for documentation, or other purposes is advantageous.  Does anything in the design of hieratika so far mandate the XML approach and a more constrained evolution of plant system metadata?
1. The load/save/commit cycle and implied associated versioning and control could potentially benefit from a git backend that gives all the git goodness like checksummed content and everything else.   Is this worth considering?  i.e. An upgrade from the existing Level-1 use of CVS version strings?   
1. Given the focus on protecting sections from multiple access, is there any risk in the distributed version of hitting NFS style issues?

## Questions to Self

1. What is the syntax standard for the .ini file?
1. Permissions/access control - do we call this RBAC?

## Tools and Coding Standards

Many of the following are minor/pedantic/low priority comments.  Also much is easily delegated to domain novices but python experts.

1. TODO : run a python automatic documentation generator to pull out the API.
1. TODO : janitor task : review and/or supply docstrings throughout.
1. TODO : coding standards document to clarify where we adopt e.g. PEP8, camelCase, yadayada, or not.
1. TODO : from the performance time and logging, and caching, performance is an issue.  Are we using best tools?
1. TODO : code size (1199 lines) indicates opportunities for some later janitoral refactoring.
..1. QUESTION : lots of objects : to what extent should they be encapsulated in classes?
..1. COMMENT : lots of accessor methods, is there any scope for use of decorators?
..1. COMMENT : general function of the code is an ELT operation, going from XML file to in memory, transform, then back.
..1. COMMENT : file system and locking ; MRW mantra : the file system is not an IPC.  Any need to revisit?
..1. COMMENT : lots of symmetry with respect to getEntityAttribute/getEntitiesAttributes.  Review consistency.  Justify gaps.
..1. COMMENT : lots of acquire lock; critical section; release lock.  Can python "with" idiom help or would it hinder?
1. TODO : some stylistic idiom jumps out as behind the curve with respect to modern iterator python style.   e.g. for key in dictionary: value = dictionary[key].   Can be improved.

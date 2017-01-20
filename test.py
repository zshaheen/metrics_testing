import add
import sub

print '------------------------'
print 'Adding 2 and 3'
metric = add.Add()
print metric(2, 3)
print '------------------------'
print 'Adding and subtracting 2 and 3 as a compound metric'
metric2 = sub.Sub()
compound_metric = metric + metric2
print compound_metric(2, 3)
print '------------------------'
print 'Removing the subtaction from the compound metric'
compound_metric = metric + metric2
compound_metric2 = compound_metric - metric2
print compound_metric2(2, 3)

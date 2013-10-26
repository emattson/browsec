//
//  Communicator.h
//  Bastion
//
//  Created by Eli Mattson on 10/26/13.
//  Copyright (c) 2013 Eli Mattson. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface Communicator : NSObject

-(NSObject *) getWebsite;
-(NSObject *) getActionFramework;
-(void) sendAction:(NSObject *) userAction;

@end
